##############################################################################
#
#    Copyright (C) 2021  Quilsoft  (http://www.quilsoft.com)
#    All Rights Reserved.
#
##############################################################################

{
    'name': 'tronn',
    'version': '16.0.1.0.0',
    'category': 'Tools',
    'summary': "Proyect module for tronn",
    'author': "Quilsoft",
    'website': 'quilsoft.com',
    'license': 'AGPL-3',
    'depends': [
        ],
    'installable': True,

    'env-ver': '2',
    'odoo-license': 'EE',
    'config': [

        # 'addons_path' is always computed looking for the repositories in sources
        # 'data_dir' is a fixed location inside docker odoo image

        # You should use 2 worker threads + 1 cron thread per available CPU,
        # and 1 CPU per 10 concurent users.
        # if ommited oe will calculate workers and cron´s based on # of cpu
                'workers = 0',
                'max_cron_threads = 1',

        # Number of requests a worker will process before being recycled and
        # restarted. Defaults to 8192 if ommited
                'limit_request = 8192',

        # Maximum allowed virtual memory per worker. If the limit is exceeded,
        # the worker is killed and recycled at the end of the current request.
        # Defaults to 640MB
                'limit_memory_soft = 2147483648',

        # Hard limit on virtual memory, any worker exceeding the limit will be
        # immediately killed without waiting for the end of the current request
        # processing. Defaults to 768MB.
                'limit_memory_hard = 2684354560',
                'admin_passwd = admin',
    ],

    'port': '8069',

    'git-repos': [
        # Quilsoft
        'git@github.com:quilsoft-org/cl-tronn.git',
        'git@github.com:quilsoft-org/tronn.git -b main',

        # ingadhoc
        'https://github.com/ingadhoc/account-financial-tools INGADHOC/account-financial-tools',
        'https://github.com/ingadhoc/account-payment INGADHOC/account-payment',
        'https://github.com/ingadhoc/odoo-argentina INGADHOC/odoo-argentina',
        'https://github.com/ingadhoc/argentina-sale INGADHOC/argentina-sale',
        'https://github.com/ingadhoc/account-invoicing.git sub_loca/account-invoicing',
        'https://github.com/ingadhoc/odoo-argentina-ee INGADHOC/odoo-argentina-ee',
        #QUILSOFT
        'git@github.com:quilsoft-org/third-party-modules.git sub-quilsoft/third-party-modules',
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-ent:16.0e',
        'postgres postgres:15.1-alpine',
    ]
}
