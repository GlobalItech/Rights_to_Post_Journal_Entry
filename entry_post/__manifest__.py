{
    'name' : 'User Rights to post Journal Entry ',
    'author' : 'itech resources',
    'website' : 'www.itechresoureces.com',
    'description' : 'After validation inovice should be in Unposted state in Journal',
    'depends' : ['account', 'sale'],
    'version' : '1.0',
    'data' :[
                'views/post_approval.xml',
                'security/invoice_security.xml'
            ],
    'installable' : True,
    'price':'15.0',
    'currency': 'EUR',
}
