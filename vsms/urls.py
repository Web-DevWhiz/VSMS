"""vsms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vehicle import views
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView

class CustomLoginView(LoginView):
    user_type = None 

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        if self.user_type == 'customer' and not user.is_staff:
            return redirect('customer-dashboard') 
        elif self.user_type == 'mechanic' and not user.is_staff:
            return redirect('mechanic-dashboard') 
        elif self.user_type == 'admin' and user.is_staff:
            return redirect('admin-dashboard')
        else:
            return redirect('')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),

    path('adminclick', views.adminclick_view),
    path('customerclick', views.customerclick_view),
    path('mechanicsclick', views.mechanicsclick_view),

    path('customersignup', views.customer_signup_view,name='customersignup'),
    path('mechanicsignup', views.mechanic_signup_view,name='mechanicsignup'),

    path('customerlogin', CustomLoginView.as_view(template_name='vehicle/customerlogin.html', user_type='customer'), name='customerlogin'),
    path('mechaniclogin', CustomLoginView.as_view(template_name='vehicle/mechaniclogin.html', user_type='mechanic'), name='mechaniclogin'),
    path('adminlogin', CustomLoginView.as_view(template_name='vehicle/adminlogin.html', user_type='admin'), name='adminlogin'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-customer', views.admin_customer_view,name='admin-customer'),
    path('admin-view-customer',views.admin_view_customer_view,name='admin-view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
    path('admin-add-customer', views.admin_add_customer_view,name='admin-add-customer'),
    path('admin-view-customer-enquiry', views.admin_view_customer_enquiry_view,name='admin-view-customer-enquiry'),
    path('admin-view-customer-invoice', views.admin_view_customer_invoice_view,name='admin-view-customer-invoice'),


    path('admin-request', views.admin_request_view,name='admin-request'),
    path('admin-view-request',views.admin_view_request_view,name='admin-view-request'),
    path('change-status/<int:pk>', views.change_status_view,name='change-status'),
    path('admin-delete-request/<int:pk>', views.admin_delete_request_view,name='admin-delete-request'),
    path('admin-add-request',views.admin_add_request_view,name='admin-add-request'),
    path('admin-approve-request',views.admin_approve_request_view,name='admin-approve-request'),
    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    
    path('admin-view-service-cost',views.admin_view_service_cost_view,name='admin-view-service-cost'),
    path('update-cost/<int:pk>', views.update_cost_view,name='update-cost'),

    path('admin-mechanic', views.admin_mechanic_view,name='admin-mechanic'),
    path('admin-view-mechanic',views.admin_view_mechanic_view,name='admin-view-mechanic'),
    path('delete-mechanic/<int:pk>', views.delete_mechanic_view,name='delete-mechanic'),
    path('update-mechanic/<int:pk>', views.update_mechanic_view,name='update-mechanic'),
    path('admin-add-mechanic',views.admin_add_mechanic_view,name='admin-add-mechanic'),
    path('admin-approve-mechanic',views.admin_approve_mechanic_view,name='admin-approve-mechanic'),
    path('approve-mechanic/<int:pk>', views.approve_mechanic_view,name='approve-mechanic'),
    path('delete-mechanic/<int:pk>', views.delete_mechanic_view,name='delete-mechanic'),
    path('admin-view-mechanic-salary',views.admin_view_mechanic_salary_view,name='admin-view-mechanic-salary'),
    path('update-salary/<int:pk>', views.update_salary_view,name='update-salary'),

    path('admin-mechanic-attendance', views.admin_mechanic_attendance_view,name='admin-mechanic-attendance'),
    path('admin-take-attendance', views.admin_take_attendance_view,name='admin-take-attendance'),
    path('admin-view-attendance', views.admin_view_attendance_view,name='admin-view-attendance'),
    path('admin-feedback', views.admin_feedback_view,name='admin-feedback'),

    path('admin-report', views.admin_report_view,name='admin-report'),

    path('mechanic-dashboard', views.mechanic_dashboard_view,name='mechanic-dashboard'),
    path('mechanic-work-assigned', views.mechanic_work_assigned_view,name='mechanic-work-assigned'),
    path('mechanic-update-status/<int:pk>', views.mechanic_update_status_view,name='mechanic-update-status'),
    path('mechanic-feedback', views.mechanic_feedback_view,name='mechanic-feedback'),
    path('mechanic-salary', views.mechanic_salary_view,name='mechanic-salary'),
    path('mechanic-profile', views.mechanic_profile_view,name='mechanic-profile'),
    path('edit-mechanic-profile', views.edit_mechanic_profile_view,name='edit-mechanic-profile'),

    path('mechanic-attendance', views.mechanic_attendance_view,name='mechanic-attendance'),



    path('customer-dashboard', views.customer_dashboard_view,name='customer-dashboard'),
    path('customer-request', views.customer_request_view,name='customer-request'),
    path('customer-add-request',views.customer_add_request_view,name='customer-add-request'),

    path('customer-profile', views.customer_profile_view,name='customer-profile'),
    path('edit-customer-profile', views.edit_customer_profile_view,name='edit-customer-profile'),
    path('customer-feedback', views.customer_feedback_view,name='customer-feedback'),
    path('customer-invoice', views.customer_invoice_view,name='customer-invoice'),
    path('customer-view-request',views.customer_view_request_view,name='customer-view-request'),
    path('customer-delete-request/<int:pk>', views.customer_delete_request_view,name='customer-delete-request'),
    path('customer-view-approved-request',views.customer_view_approved_request_view,name='customer-view-approved-request'),
    path('customer-view-approved-request-invoice',views.customer_view_approved_request_invoice_view,name='customer-view-approved-request-invoice'),

    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='vehicle/index.html'),name='logout'),

    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
]
