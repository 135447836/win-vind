# coding: utf-8

from transitions.extensions import GraphMachine


class Model(object):
    pass


states = [
    'Waiting first inputs',
    'Parse head number',
    'Waiting first inputs without parsing number',
    'Waiting inputs',
    'Accepted'
]

get_states = {
    'first_wait_wnum': states[0],
    'parse_num': states[1],
    'first_wait': states[2],
    'wait': states[3],
    'acc': states[4],
}

transitions = [
    # Initial
    {
        'trigger': 'Empty',
        'source': get_states['first_wait_wnum'],
        'dest': get_states['first_wait_wnum']
    },
    {
        'trigger': 'Numbers except for zero',
        'source': get_states['first_wait_wnum'],
        'dest': get_states['parse_num']
    },
    {
        'trigger': 'Except for numbers',
        'source': get_states['first_wait_wnum'],
        'dest': get_states['wait']
    },

    # Initial Waiting
    {
        'trigger': 'Empty',
        'source': get_states['first_wait'],
        'dest': get_states['first_wait_wnum']
    },
    {
        'trigger': 'Numbers only except for zero',
        'source': get_states['first_wait'],
        'dest': get_states['first_wait']
    },
    {
        'trigger': 'Except for numbers',
        'source': get_states['first_wait'],
        'dest': get_states['wait']
    },

    # Waiting
    {
        'trigger': 'Input',
        'source': get_states['wait'],
        'dest': get_states['wait']
    },

    # Accepted
    {
        'trigger': 'Empty',
        'source': get_states['acc'],
        'dest': get_states['first_wait_wnum']
    },
    {
        'trigger': 'Same as previous',
        'source': get_states['acc'],
        'dest': get_states['acc']
    },
    {
        'trigger': 'Input differently (ε-transitions)',
        'source': get_states['acc'],
        'dest': get_states['first_wait']
    },

    # Parse number
    {
        'trigger': 'Empty',
        'source': get_states['parse_num'],
        'dest': get_states['parse_num']
    },
    {
        'trigger': 'Numbers',
        'source': get_states['parse_num'],
        'dest': get_states['parse_num']
    },
    {
        'trigger': 'Except for numbers',
        'source': get_states['parse_num'],
        'dest': get_states['wait']
    }
]

model = Model()
machine = GraphMachine(
        model=model,
        states=states,
        transitions=transitions,
        initial=get_states['first_wait_wnum'],
        title='NTypeLogger State Transition Diagram')


graph = model.get_graph()
graph.draw('ntype_logger_state_transition_diagram.png', prog='dot')
