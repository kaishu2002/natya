from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
from django.views.generic.edit import *
from django.contrib.auth import authenticate,load_backend,logout,login
from django.views.generic.edit import * 
from django.views.generic import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout as auth_logout
from django.urls import reverse_lazy
from . forms import*
from .models import *
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the gurus who are approved
        approved_gurus = Register.objects.filter(is_approved=True,usertype=2)
        # Pass the approved gurus to the context
        context['approved_gurus'] = approved_gurus
        return context

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data["email"]
            # Check if user with this email already exists
            if Register.objects.filter(email=email).exists():
                # If user already exists, handle accordingly (e.g., redirect to login with message)
                form = LoginForm()
                return render(request, 'login.html', {'form': form, 'z': True})
            else:
                try:
                    # Create new user
                    k= form.save(commit=False)
                    k.password=make_password(form.cleaned_data['password'])
                    k.usertype=0
                    k.is_active=True
                    k.save()
                    messages.success(request, 'Your registration has been successful! You can login now.')
                    return redirect('/login')
                except Exception as e:
                    # Handle exceptions during form.save()
                    form.add_error(None, f'An error occurred while saving the form: {e}')
        else:
            # Form is invalid, handle errors
            return render(request, 'register.html', {'form': form})
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})

def doLogin(request):
    form = LoginForm()
    if request.method == "POST":
        user = authenticate(request,username=request.POST["username"],password=request.POST["password"] )
        print(user)
        if user is None:
            print("kjmhn bk,m")
            return render(request,'index.html',{'form':form,'k':True})   
        else:
            login(request, user)
            data = Register.objects.get(username=user)
            print(data)
            request.session['ut']=data.usertype
            data.usertype
            request.session['uid']=data.id
            print(data.usertype)
            messages.success(request, f'Login Successfull!! Welcome {data.username}', extra_tags='log')
            return redirect('/')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})
    



class ContactView(TemplateView):
    template_name = 'contact.html'

def guru_register(request):
    if request.method == 'POST':
        form = GuruRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data['password']
            user.set_password(password)  # Use set_password to save the hashed password correctly
            user.is_active=False

         
            user.usertype = 2
            user.save()

            return redirect('/login')  # Make sure this URL exists and is correctly configured
        else:
            # Optional: Print form errors to debug
            print(form.errors)
    else:
        form = GuruRegistrationForm()

    return render(request, 'gurureg.html', {'form': form})



class ApproveGurusView(View):
    template_name = 'approve_guru.html'

    def test_func(self):
        # Ensure only staff members can access this view
        return self.request.user.is_staff

    def get(self, request):
        # Fetch all gurus that are not yet approved
        gurus = Register.objects.filter(is_approved=False, usertype=2)
        context = {
            'gurus': gurus
        }
        return render(request, self.template_name, context)

    def post(self, request):
        guru_id = request.POST.get('guru_id')
        action = request.POST.get('action')

        if not guru_id or action not in ['approve', 'reject']:
            messages.error(request, "Invalid action or Guru ID.")
            return redirect('approve_gurus')

        try:
            guru = Register.objects.get(id=guru_id, usertype=2)  # Ensure the guru exists and is a guru
        except Register.DoesNotExist:
            messages.error(request, "Guru not found.")
            return redirect('approve_gurus')

        if action == 'approve':
            guru.is_approved = True
            guru.is_active = True
            guru.save()
            messages.success(request, "Guru approved successfully.")
        elif action == 'reject':
            guru.delete()
            messages.success(request, "Guru rejected and deleted successfully.")

        return redirect('approve_gurus')





def guru_dashboard(request):
    if not request.user.is_authenticated or not request.user.guru.is_approved:
        return redirect('login')
    


def Logout(request):
    print("jhcfhgfhvyvftuvgthcvhgvchgvhgv")
    auth.logout(request)                
    return redirect('/')



class ViewUsersAndGurus(TemplateView):
    template_name = 'views_users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Fetch all users and gurus
        context['users'] = Register.objects.filter(usertype=0)
        context['gurus'] = Register.objects.filter(usertype=2)
        
        # Check if a specific user or guru ID is provided in the URL
        user_id = self.kwargs.get('user_id')
        guru_id = self.kwargs.get('guru_id')
        
        if user_id:
            # Fetch the specific user registration
            context['specific_user'] = get_object_or_404(Register, id=user_id, usertype=0)
        if guru_id:
            # Fetch the specific guru registration
            context['specific_guru'] = get_object_or_404(Register, id=guru_id, usertype=2)
        
        return context
    
class SelectViews(TemplateView):
    template_name = 'page.html'

# USER PROFILE
class UserProfileView(DetailView):
    model = Register
    template_name = 'profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return Register.objects.get(id=self.request.user.id)


class UpdateProfileView(UpdateView):
    model = Register
    form_class = UserProfileForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return Register.objects.get(id=self.request.user.id)
    
# GURU PROFILE
class GuruProfileView(UpdateView):
    model = Register
    fields = ['email', 'phone', 'image']  # Ensure 'fields' attribute is set
    template_name = 'updateg_profile.html'
    success_url = reverse_lazy('guruprofile')  # Redirect to profile page after update

    def get_object(self):
        return self.request.user


class ProfileView(UpdateView):
    model = Register
    template_name = 'updateg_profile.html'
    success_url = reverse_lazy('profile')  

    def get_object(self):
        return self.request.user
from django.contrib.auth import *



class ResetPasswordView(FormView):
    template_name = 'reset_password.html'
    form_class = ResetPassword
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the current user to the form
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        form.save()
        update_session_auth_hash(self.request, user)  # Prevent logout
        return super().form_valid(form)
    

class GuruViewMore(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        approved_gurus = Register.objects.filter(is_approved=True,usertype=2)
        context['approved_gurus'] = approved_gurus
        return context
    
  
class GuruDetailView(DetailView):
    model = Register
    template_name = 'guru_details.html'
    context_object_name= 'guru'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        approved_gurus = Register.objects.filter(is_approved=True,usertype=2)
        context['approved_gurus'] = approved_gurus
        return context
 

class GuruCreatView(CreateView):
    model = Register
    template_name = 'guru_form.html'
    fields = ['about', 'style', 'journey', 'academic_details']  # Add other fields as necessary
    success_url = '/gurus/'  # Redirect after update

class GuruListView(ListView):
    model = Register
    template_name = 'guru_list.html'

# def cnt(request):
#     if request.method=='POST':
#         name=request.GET.get('name')
#         name=request.POST['name']
#         eamil=request.POST['email']
#         subject=request.POST['subject']
#         message=request.POST['msg']
#         print('name :',name)
#         Contact.objects.create(
#             name=name,
#             email=eamil,
#             subject=subject,
#             message=message
#         )
#     return render(request,'cnt.html')



# def cnt(request):
#     cntform=ContactForm(request.POST,request.FILES)
#     if request.method=='POST':
#         if cntform.is_valid():
#             print("inside the form")
#             cntform.save()
#             return redirect('/')
#         else:
#             print(cntform.errors)
#     else:
#         print("in else")
#         cntform=ContactForm()
#     return render(request,'cnt.html',{'cnnn':cntform})



class ContactUser(TemplateView):
    template_name = 'cnt.html'
    form_class = ContactForm
    context_object_name = 'cnnn'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = self.form_class()
        return context
    


class Bharatanatyamview(TemplateView):
    template_name = 'bharatanatyam.html'
