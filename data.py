origins = [
    {
        'url': 'http://example.com',
        'name': 'google',
        'visits': [
            {
                'status': 'success',
                'snapshot': {
                    'date': '10/10/2010',
                    'revisions': [
                        {
                            'message': 'first revision',
                        },
                        {
                            'message': 'second revision',
                        },
                    ],
                },
            },

            {
                'status': 'success',
                'snapshot': {
                    'date': '12/10/2010',
                    'revisions': [
                        {
                            'message': 'first revision',
                        },
                        {
                            'message': 'second revision',
                        },
                        {
                            'message': 'third revision',
                        },
                    ],
                },
            },

        ],
    },
    {
        'url': 'http://swh.org',
        'name': 'swh',
        'visits': [
            {
                'status': 'failed',
                'snapshot': {
                    'date': '06/12/2020',
                    'revisions': [],
                },
            },
        ]
    },
]
