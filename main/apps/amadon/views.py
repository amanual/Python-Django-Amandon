from django.shortcuts import render, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    # print request.POST['product_id']
    

    return render(request, 'amadon/index.html')
    
def amadon(request):
    
    print int(request.POST['quantity'])
    result = int(request.POST['quantity'])    
       
    if 'count' in request.session: 
        # request.session['count'] += request.session['count'] 
        # request.session['total'] += request.session['total']
        print request.session['total'] 
        print request.session['count']   

        if 'quantity' in request.POST and request.POST['product_id'] == '1015':            
            request.session['iphone']= result * 700            
            request.session['count'] += result
            request.session['total'] += request.session['iphone']

        if 'quantity' in request.POST and request.POST['product_id'] == '1016':                
            request.session['iphone']= result * 800
            request.session['count'] += result
            request.session['total'] += request.session['iphone']
            
        if 'quantity' in request.POST and request.POST['product_id'] == '1017':                
            request.session['iphone']= result * 900
            request.session['count'] += result
            request.session['total'] += request.session['iphone']

        if 'quantity' in request.POST and request.POST['product_id'] == '1018':                
            request.session['iphone']= result * 1000
            request.session['count'] += result
            request.session['total'] += request.session['iphone']

        
        
    return render(request, 'amadon/display.html')
# def reset(request):
#     request.session.clear()
#     return redirect('/')
