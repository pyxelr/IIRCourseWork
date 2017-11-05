RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['PATCH', 'DELETE']

DOMAIN = {


    'user': {
        'schema': {
            'firstname': {
                'type': 'string'
            },
            'lastname': {
                'type': 'string'
            },
            'username': {
                'type': 'string',
                 'unique': True
            },
            'password': {
                'type': 'string'
            },
            'phone': {
                'type': 'string'
            }

        },

        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'username'
        }
    },


    'article': {
        'schema': {
            'title': {
                'type': 'string'
            },
            'content': {
                'type': 'string'
            },
            'category': {
                'type': 'dict',
                'schema': {
                    'catName': {
                        'type': 'string',
                        'data_relation': {
                        'resource': 'category',
                        'field': 'catName',
                        'embeddable': True
                    }
                }
            }
            },
            'uid': {
                'type': 'dict',
                'schema': {
                    'username': {
                        'type': 'string',
                        'data_relation': {
                        'resource': 'user',
                        'field': 'username',
                        'embeddable': True
                    }
                }
            }
            },

            'additional_lookup': {
        	'url': 'regex("[\w]+")',
        	'field': 'category'
    	   },
    
		  'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'uid'
            }
    }
    },
    

    'category': {
        'schema': {
            
            'catName': {
                'type': 'string'
            }
        }
    },

    'item': {
        'schema': {
            'name':{
                'type': 'string'
            },
            'username': {
                'type': 'string'
            }
        }
    }

}