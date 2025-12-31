MONGO_URI = "mongodb://localhost:27017/tododb"

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

DOMAIN = {
    'tasks': {
        'schema': {
            'title': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 300,
                'required': True,
                'empty': False,
            },
            'description': {
                'type': 'string',
                'maxlength': 1000,
                'required': False,
            },
            'status': {
                'type': 'string',
                'allowed': ['todo', 'in_progress', 'done'],
                'default': 'todo',
                'required': True,
            }
        }
    }
}
