from flasgger import APISpec

spec = APISpec(
    title='Get-Terra-Server-for-Admin',
    version='0.10.1',
    plugins=[
        'apispec.ext.flask',
        'apispec.ext.marshmallow'
    ]
)
