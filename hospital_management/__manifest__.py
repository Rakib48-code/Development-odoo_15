{
    'name': 'Hospital Management System',
    'category': 'Healthcare',
    'version': '1.0',
    'author': 'Rakib Hasan',
    'summary': 'An efficient solution for managing hospital operations, including patient records, appointments, billing, and staff management.',
    'description': """
        This Hospital Management System streamlines hospital processes by offering features such as patient management, 
        appointment scheduling, staff and payroll management, billing, and medical inventory tracking. 
        It is designed to be user-friendly and adaptable for hospitals of varying sizes.
    """,
    'depends': ['base'],
    'data': [
        'views/hospital_menu_view.xml',
        'views/patient_view_menu.xml',
        'views/female_patient_view.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'sequence': -100
}
