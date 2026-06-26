
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # path('', views.dashboard, name='dashboard'),

    path(
        'medicines/',
        views.medicine_list,
        name='medicine_list'
    ),

    path(
        'add-medicine/',
        views.add_medicine,
        name='add_medicine'
    ),

    path(
        'update-medicine/<int:id>/',
        views.update_medicine,
        name='update_medicine'
    ),

    path(
        'delete-medicine/<int:id>/',
        views.delete_medicine,
        name='delete_medicine'
    ),


    path(
        'suppliers/',
        views.supplier_list,
        name='supplier_list'
    ),

    path(
        'add-supplier/',
        views.add_supplier,
        name='add_supplier'
    ),

    path(
        'update-supplier/<int:id>/',
        views.update_supplier,
        name='update_supplier'
    ),

    path(
        'delete-supplier/<int:id>/',
        views.delete_supplier,
        name='delete_supplier'
    ),

    path(
        'invoice/',
        views.invoice_pdf,
        name='invoice'
    ),

    path('login/', 
        views.login_page, 
        name='login'
    ),

    path('logout/',
        views.logout_page,
        name='logout'
    ),

    path('billing/',
        views.billing,
        name='billing'
    ),

    path(
        'bill-history/',
        views.bill_history,
        name='bill_history'
    )
    ,
    path(
        'delete-bill/<int:id>/',
        views.delete_bill,
        name='delete_bill'
    ),
    path(
        'invoice/<int:id>/',
        views.invoice,
        name='invoice'
    ),

    path(
        'invoice-pdf/<int:id>/',
        views.invoice_pdf,
        name='invoice_pdf'
    ),

    path(
        'stock-history/',
        views.stock_history,
        name='stock_history'
    ),
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),
    path('', views.login_page, name='login'),
    path(
    'sales-report/',
    views.sales_report,
    name='sales_report'
),
path(
    'sales-report/pdf/',
    views.sales_report_pdf,
    name='sales_report_pdf'
),
path(
    'sales-report/excel/',
    views.sales_report_excel,
    name='sales_report_excel'
),
path(
    'sales-prediction/',
    views.sales_prediction,
    name='sales_prediction'
),
path(
    'inventory-report/',
    views.inventory_report,
    name='inventory_report'
),
path(
    'inventory-report/pdf/',
    views.inventory_report_pdf,
    name='inventory_report_pdf'
),
path(
    'profile/',
    views.profile,
    name='profile'
),
path(
    'settings/',
    views.settings_page,
    name='settings'
),
path(
    'edit-profile/',
    views.edit_profile,
    name='edit_profile'
),
path(
    'settings/',
    views.settings_page,
    name='settings'
),
path(
    'change-password/',
    views.change_password,
    name='change_password'
),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )