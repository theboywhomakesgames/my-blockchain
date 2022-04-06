from block import Block
import PySimpleGUI as sg
import json

def print_block(blk):
    print(json.dumps({
        'prehash': blk.pre_hash,
        'transaction': blk.transaction,
        'salt': blk.salt,
        'timestamp': blk.timestamp,
        'hash': blk.hash,
        'nonce': blk.nonce
    }))

layout = [
    [sg.Multiline(size=(110, 10), key='-input-'), sg.Button('process'), sg.Button('gen')],
    [sg.Input('transaction', key='-tr-'), sg.Button('transact')]
]

window = sg.Window('socket connection', layout)
blocks = []

def update_window(window):
    layout = [
        [sg.Multiline(size=(110, 10), key='-input-'), sg.Button('process'), sg.Button('gen')],
        [sg.Input('transaction', key='-tr-'), sg.Button('transact')]
    ]
    loc = window.current_location()
    window.close()
    for b in blocks:
        layout.append(
            [sg.Text('tr: ' + b.transaction)]
        )
    w = sg.Window('socket connection', location=loc).Layout(layout)
    return w

while True:
    event, value = window.read()
    if event == 'gen':
        if len(blocks) == 0:
            blk = Block('0', '%0%0%100%')
            blk.solve()
            print_block(blk)
            blocks.append(blk)
        window = update_window(window)

    if event == 'process':
        blkjson = json.loads(value['-input-'])
        if len(blocks) == 0:
            blk = Block(blkjson['prehash'], blkjson['transaction'])
            blk.nonce = blkjson['nonce']
            blk.timestamp = blkjson['timestamp']
            blk.salt = blkjson['salt']
            blk.hash = blkjson['hash']
            blocks.append(blk)
            print("block added")
        else:
            blk = Block(blocks[len(blocks) - 1].hash, blkjson['transaction'])
            if blk.setParams(blocks[len(blocks) - 1].hash, blkjson['transaction'], blkjson['salt'], blkjson['timestamp'], blkjson['hash'], blkjson['nonce']):
                print("block successfully added")
                print(blkjson)
                blocks.append(blk)
            else:
                with open('ilwyl.txt', 'r') as f:
                    print(f.read())
        window = update_window(window)

    if event == 'transact':
        blk = Block(blocks[len(blocks) - 1].hash, value['-tr-'])
        blk.solve()
        print_block(blk)
        blocks.append(blk)
        window = update_window(window)

    if event == sg.WIN_CLOSED:
        break
