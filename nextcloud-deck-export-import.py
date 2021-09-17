import requests
urlFrom = 'https://cloud.website.com'
authFrom = ('user', 'password')
headers={'OCS-APIRequest': 'true', 'Content-Type': 'application/json'}

def getBoards():
    response = requests.get(
            f'{urlFrom}/index.php/apps/deck/api/v1.0/boards',
            auth=authFrom,
            headers=headers)
    response.raise_for_status()
    return response.json()

def getBoardDetails(boardId):
    response = requests.get(
            f'{urlFrom}/index.php/apps/deck/api/v1.0/boards/{boardId}',
            auth=authFrom,
            headers=headers)
    response.raise_for_status()
    return response.json()

def getStacks(boardId):
    response = requests.get(
            f'{urlFrom}/index.php/apps/deck/api/v1.0/boards/{boardId}/stacks',
            auth=authFrom,
            headers=headers)
    response.raise_for_status()
    return response.json()

def getStacksArchived(boardId):
    response = requests.get(
            f'{urlFrom}/index.php/apps/deck/api/v1.0/boards/{boardId}/stacks/archived',
            auth=authFrom,
            headers=headers)
    response.raise_for_status()
    return response.json()

def createBoard(title, color):
    response = requests.post(
            f'{urlTo}/index.php/apps/deck/api/v1.0/boards',
            auth=authTo,
            json={
                'title': title,
                'color': color
            },
            headers=headers)
    response.raise_for_status()
    board = response.json()
    boardId = board['id']
    # remove all default labels
    for label in board['labels']:
        labelId = label['id']
        response = requests.delete(
            f'{urlTo}/index.php/apps/deck/api/v1.0/boards/{boardId}/labels/{labelId}',
            auth=authTo,
            headers=headers)
        response.raise_for_status()
    return board

def createLabel(title, color, boardId):
    response = requests.post(
            f'{urlTo}/index.php/apps/deck/api/v1.0/boards/{boardId}/labels',
            auth=authTo,
            json={
                'title': title,
                'color': color
            },
            headers=headers)
    response.raise_for_status()
    return response.json()

def createStack(title, order, boardId):
    response = requests.post(
            f'{urlTo}/index.php/apps/deck/api/v1.0/boards/{boardId}/stacks',
            auth=authTo,
            json={
                'title': title,
                'order': order
            },
            headers=headers)
    response.raise_for_status()
    return response.json()

def createCard(title, ctype, order, description, duedate, boardId, stackId):
    response = requests.post(
            f'{urlTo}/index.php/apps/deck/api/v1.0/boards/{boardId}/stacks/{stackId}/cards',
            auth=authTo,
            json={
                'title': title,
                'type': ctype,
                'order': order,
                'description': description,
                'duedate': duedate
            },
            headers=headers)
    response.raise_for_status()
    return response.json()

def assignLabel(labelId, cardId, boardId, stackId):
    response = requests.put(
            f'{urlTo}/index.php/apps/deck/api/v1.0/boards/{boardId}/stacks/{stackId}/cards/{cardId}/assignLabel',
            auth=authTo,
            json={
                'labelId': labelId
            },
            headers=headers)
    response.raise_for_status()

def archiveCard(card, boardId, stackId):
    cardId = card['id']
    card['archived'] = True
    response = requests.put(
            f'{urlTo}/index.php/apps/deck/api/v1.0/boards/{boardId}/stacks/{stackId}/cards/{cardId}',
            auth=authTo,
            json=card,
            headers=headers)
    response.raise_for_status()

def copyCard(card, boardIdTo, stackIdTo, labelsMap):
    createdCard = createCard(
        card['title'],
        card['type'],
        card['order'],
        card['description'],
        card['duedate'],
        boardIdTo,
        stackIdTo
    )

    # copy card labels
    if card['labels']:
        for label in card['labels']:
            assignLabel(labelsMap[label['id']], createdCard['id'], boardIdTo, stackIdTo)

    if card['archived']:
        archiveCard(createdCard, boardIdTo, stackIdTo)


# get boards list
boards = getBoards()

# create boards
for board in boards:
    boardIdFrom = board['id']

    # create labels
    boardDetails = getBoardDetails(board['id'])

    # copy stacks
    stacks = getStacks(boardIdFrom)
    board['stacks'] = stacks

import json
json = json.dumps(boards, indent=4)

from contextlib import redirect_stdout
with open('/tmp/nextcloud_deck_export.json', 'w') as f:
    with redirect_stdout(f):
        print(json)