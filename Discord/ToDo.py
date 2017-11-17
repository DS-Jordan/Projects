import discord
import asyncio
import random
import pickle
import os
import time
import random

client = discord.Client()
todo_list = []
prefix = '!'
flip = random.choice(['Heads', 'False'])
assistance = ["!todo add", "!todo remove",
              "!todo read", "!todo clear", "!roll", "!flip", "!settings", '!devs']
dice = random.randint(1, 6)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith("!test"):
        await client.send_message(message.channel, ":thumbsup: ")

    elif message.content.startswith('{}todo add'.format(prefix)):
        print(todo_list[10:])
        await client.send_message(message.channel, ':arrow_forward: Added ** {} ** to the todo list :arrow_backward: '.format(str(message.content[10:])))
        todo_list.append(message.content[10:])

    elif message.content.startswith('{}todo read'.format(prefix)):
        await client.send_message(message.channel, ':arrow_forward:  _** To-do List **_ :arrow_backward:')
        if len(todo_list) != 0:
            num = 0
            for i in todo_list:
                num = num + 1
                await client.send_message(message.channel, '{} {}'.format(str(':hammer:'), i))
        else:
            await client.send_message(message.channel, ':arrow_forward: The To-Do list is empty! :arrow_backward:')

    elif message.content.startswith('{}todo remove'.format(prefix)):
        if len(todo_list) != 0:  # if list has > than 0 items in it
            # Finding item in list and returning it's position
            listitem = message.content[13:]
            index_number = todo_list.index(listitem)
            del todo_list[index_number]
            await client.send_message(message.channel, '{} was removed from the To-Do list'.format(str(message.content[13:])))
        else:
            await client.send_message(message.channel, ':arrow_forward: To-Do list is empty! :arrow_backward:')

    elif message.content.startswith('{}todo clear'.format(prefix)):
        if len(todo_list) != 0:
            todo_list.clear()
            await client.send_message(message.channel, ':arrow_forward: To-Do list was cleared! :arrow_backward:')
        else:
            await client.send_message(message.channel, ':arrow_forward: To-Do list is empty! :arrow_backward:')

    elif message.content.startswith('{}flip'.format(prefix)):
        await client.send_message(message.channel, flip)

    elif message.content.startswith('{}roll'.format(prefix)):
        await client.send_message(message.channel, 'you rolled a {}:game_die:'.format(str(dice)))

    elif message.content.startswith('{}dip help'.format(prefix)):
        await client.send_message(message.channel, ':arrow_forward: **Commands** :arrow_backward: ')
        if len(assistance) != 0:
            num = 0
            for i in assistance:
                num = num + 1
                await client.send_message(message.channel, '**{}: {}**'.format(str(":speaking_head:"), i))

    elif message.content.startswith('{}devs'.format(prefix)):
        await client.send_message(message.channel, ':wrench: DrSkullduggery & Kiwan :wrench:')

    elif message.content.startswith('{}settings'.format(prefix)):
        await client.send_message(message.channel, ' :gear: ** There are None, Peasant** :gear:')
client.run("Insert Code Here")
