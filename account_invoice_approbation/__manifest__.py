# Copyright 2020 TechnoLibre. (https://technolibre.ca)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Approbation invoice in draft mode to confirm it",
    "summary": "Approbation invoice in draft mode to confirm it",
    "version": "12.0.0.0.0",
    "category": "Accounting & Finance",
    # "website": "https://github.com/OCA/account-invoicing",
    "author": "TechnoLibre",
    "installable": True,
    "depends": [
        'account',
    ],
    "license": "AGPL-3",
    "data": [
        'views/account_portal_templates.xml',
    ],
}
