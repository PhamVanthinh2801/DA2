from django.shortcuts import render, get_object_or_404
from .models  import Product,InfomationUsers,Order,Myorder,Payment,ChooseSizeColor,Address,Comment
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,View
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .form import PaymentFrom,Choosesize,CheckoutFrom,AddressForm,Commentform
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import mixins
# Create your views here.

class PostList(ListView):
    queryset=Product.objects.all()
    template_name='Contents/index.html'
    context_object_name='Contents'
    paginate_by=4
class Offline(ListView):
    queryset=Product.objects.all()
    template_name='Contents/offline.html'
    context_object_name='Contents'
    paginate_by=4    
class List_giay_nu(ListView):
    queryset=Product.objects.filter(category = "SG")
    template_name='Contents/giaycaogotnu.html'
    context_object_name='giaynu'
    paginate_by = 4
class List_giay_nam(ListView):
    queryset=Product.objects.filter(category = "SB")
    template_name='Contents/giaydanam.html'
    context_object_name='giaynam'
    paginate_by = 4
class List_giay_begai(ListView):
    queryset=Product.objects.filter(category = "SK")
    template_name='Contents/giaychobegai.html'
    context_object_name='begai'
    paginate_by = 4

@login_required 
def themgiohang(request,slug):
    product = get_object_or_404(Product,slug=slug)
    C=Payment.objects.filter(user=request.user)
    b=ChooseSizeColor.objects.filter(user=request.user,Product=product,status=False)
    date = timezone.now()
    d = ProductDetail(request,product.slug)
    if request.method =="POST":
        form =Choosesize(request.POST or None)
        #print(request.POST)
        if form.is_valid():
            productsize=form.cleaned_data.get('productsize')
            productColor=form.cleaned_data.get('producColor')
            #print(productsize)
            #print(productColor)
    K=Order.objects.filter(user=request.user,product=product,status=False)
    print(product)
    print(productsize)
    print(productColor)
    if b.exists():
        b=ChooseSizeColor.objects.filter(user=request.user,Product=product,status=False, producsize=productsize, producColor=productColor)
        print(len(b))
        b = b.first()
    else:
        b=""

    print("lalalalalal")
    print(b)
    D=Order.objects.filter(user=request.user,product=product,status=False,choosesizecolor=b)#trang dụ bị trùng giữ đặt hàng và chưa đặt hàng
    if D.exists():
        date = timezone.now()
        Myorder_product,created  = Order.objects.get_or_create(product=product,user=request.user,status=False,choosesizecolor=b)#get_or_create khi nó tồn tại thì xoa đi
        # Myorder_product.choosesizecolor=b
        # Myorder_product.save()
    else:
        date = timezone.now()
        Myorder_product =Order.objects.create(product=product,user=request.user,status=False,choosesizecolor=b)
        Myorder_product.choosesizecolor=b
        Myorder_product.save()
    queryset=Myorder.objects.filter(user=request.user,status=False)
    if queryset.exists():
        myorder=queryset[0]
        if myorder.products.filter(product__slug=product.slug,status=False,choosesizecolor=b).exists():
            Myorder_product.number += 1
            Myorder_product.save()
            messages.success(request, "Bạn đã vừa thêm một sản phẩm vào giỏ hàng")
            return redirect("Contents:giohang")
        else:
            myorder.products.add(Myorder_product)
            messages.success(request, "Bạn đã vừa thêm một sản phẩm vào giỏ hàng")
            return redirect("Contents:giohang")
    else:
        date = timezone.now()
        myorder=Myorder.objects.create(user=request.user,date=date)
        myorder.products.add(Myorder_product)
        messages.success(request, "Bạn đã vừa thêm một sản phẩm vào giỏ hàng")
        return redirect("Contents:giohang")
    return redirect("Contents:productdetail",slug=slug)
@login_required
def muangay(request,slug):
    product = get_object_or_404(Product,slug=slug)#ở thư mục urls post path
    # a=Myorder.objects.filter(user=request.user,status=True)
    C=Payment.objects.filter(user=request.user)
    date = timezone.now()
    D=Order.objects.filter(user=request.user,product=product,status=False)#trang dụ bị trùng giữ đặt hàng và chưa đặt hàng
    if D.exists():
        date = timezone.now()
        Myorder_product,created  = Order.objects.get_or_create(product=product,user=request.user,status=False)#get_or_create khi nó tồn tại thì xoa đi
    else:
        date = timezone.now()
        Myorder_product =Order.objects.create(product=product,user=request.user,status=False)
    queryset=Myorder.objects.filter(user=request.user,status=False)
    if queryset.exists():
        myorder=queryset[0]
        if myorder.products.filter(product__slug=product.slug,status=False).exists():
            Myorder_product.number += 1
            Myorder_product.save()
            messages.success(request, "Bạn đã vừa thêm một sản phẩm vào giỏ hàng")
            return redirect("Contents:giohang")
            print(1)
        else:
            myorder.products.add(Myorder_product)
            messages.success(request, "Bạn đã vừa thêm một sản phẩm vào giỏ hàng")
            print(2)
            return redirect("Contents:giohang")
    else:
        date = timezone.now()
        myorder=Myorder.objects.create(user=request.user,date=date)
        myorder.products.add(Myorder_product)
        messages.success(request, "Bạn đã vừa thêm một sản phẩm vào giỏ hàng")
        return redirect("Contents:giohang")
    return redirect("Contents:productdetail",slug=slug)
@login_required
def giohang(request):
    try:
        myorder=Order.objects.filter(user=request.user,status=False)
        total1=0
        total=0
        for i in myorder:
            total1=i.number * i.product.price
            total=total+total1
        context = {
            'myorder': myorder,
            'total':total
        }
        return render(request, 'Contents/giohang.html',context)
    except ObjectDoesNotExist:
        messages.warning(request, "You do not have an active order")
        return redirect('')
@login_required #The easiest fix is to use the login_required decorator, to make sure that only logged-in users can access the view.
def themsoluongsanpham(request, slug):
    product = get_object_or_404(Product,slug=slug)#ở thư mục urls post path
    queryset=Myorder.objects.filter(user=request.user,status=False)
    D=Order.objects.filter(user=request.user,status=False)
    Myorder_product,created  = Order.objects.get_or_create(product=product,user=request.user,status=False)
    print(queryset)
    if queryset.exists():
        # myorder=queryset[0]#lấy tên người add ra chỉ có user mới có producs còn quruset ko có 
        Myorder_product.number += 1
        Myorder_product.save()
        messages.success(request, "Bạn đã vừa thêm một sản phẩm vào giỏ hàng")
        return redirect("Contents:giohang")
    return redirect("Contents:giohang")
@login_required
def xoasoluongsanpham(request,slug):
    product = get_object_or_404(Product,slug=slug)#ở thư mục urls post path
    queryset=Myorder.objects.filter(user=request.user, status=False)#Find all the groups with a member whose name starts with "user"
    if queryset.exists():
        # kiểm tra xem thằng order_product có trong myorder không 
        # nếu có tìm thằng prduct hiện tại mà ta cần xóa có trong tất cả thằng order product nếu có thì xóa  
        Myorder_product = Order.objects.filter(
            product=product,
            user=request.user,
            status=False,
        )[0]#thằng [0] có nghĩa là nó lấy ra thằng product
        if Myorder_product.number > 1:
            Myorder_product.number=Myorder_product.number-1
            Myorder_product.save()
            print("hihihihihihhi")
        else:
            print("có nè")  
            Myorder_product.delete()
            messages.success(request, "Bạn đã vừa mới xóa một sản phẩm trong giỏ hàng")
            return redirect("Contents:giohang")
    else:
        print("caicaiciaicaiciaciaicaiciaciaciaciai")
        return redirect("Contents:giohang")
    return redirect("Contents:giohang")
def thanhtoan(request):
    D=Order.objects.filter(user=request.user,status=False)
    F=Address.objects.filter(user=request.user)
    if D.exists():
        a=InfomationUsers.objects.filter(user=request.user)
        myorder = Myorder.objects.get(user=request.user,status=False)
        if a.exists() :
            myorder1 = Myorder.objects.get(user=request.user,status=False)
            queryset= InfomationUsers.objects.get(user=request.user)
            myorder1.InfomationUsers=queryset
            myorder1.save()
        else:
            messages.success(request, "mời bạn nhập thông tin chi tiết bên profile")
            return render(request, 'Contents/giohang.html')
        form =PaymentFrom(request.POST or None)      
        if request.method =="POST":
            if form.is_valid():
                if a.exists():
                    adress=queryset.adress
                    phone=queryset.phone
                    bridday=queryset.bridday
                    gender=queryset.gender
                    identify=queryset.identify
                    address = get_object_or_404(Address, pk=request.POST.get('item_id'))
                    paymentoption=form.cleaned_data.get('paymentoption')
                else:
                    messages.success(request, "mời bạn nhập đầy đủ thông tin bên phía profile")
                    return redirect("Contents:thanhtoan")
                payment=Payment(
                    user=request.user,
                    adress=adress,
                    gender=gender,
                    phone=phone,
                    bridday=bridday,
                    identify=identify,
                    paymentoption=paymentoption,
                    address=address
                )
                b=Payment.objects.filter(user=request.user)
                myorder2=Order.objects.filter(user=request.user,status=False)
                Addsizecolor=ChooseSizeColor.objects.filter(user=request.user,status=False)
                Addsizecolor.update(status=True)
                for K in Addsizecolor:
                    K.save()
        
                myorder2.update(status=True)
                for i in myorder2:
                    i.save()

                if b.exists():
                    payment.save()
                    myorder.status=True
                    myorder.Payment=payment
                    myorder.Address=payment.address
                    myorder.save()
                    messages.success(request, "Bạn đã cập nhập thanh toán thành Công")
                    return redirect("Contents:thanhtoan")
                else:
                    payment.save()
                    myorder.status=True
                    myorder.Payment=payment
                    myorder.Address=payment.address
                    myorder.save()
                    messages.success(request, "Bạn đã thanh toán thành Công")
                    return redirect("Contents:thanhtoan")
        myorder2=Order.objects.filter(status=False)
        total1=0
        total=0
        for i in myorder2:
            total1=i.number * i.product.price
            total=total+total1
        return render(request, 'Contents/thanhtoan.html',{'form':form,'myorder': D,'InfomationUsers':queryset,'email':myorder,'total':total,'addaddress':F})
    else:
        return render(request, 'Contents/giohang.html')
    return render(request, 'Contents/giohang.html')
def profile(request):
    G=Myorder.objects.filter(user=request.user,status=False)
    D=InfomationUsers.objects.filter(user=request.user)
    if G.exists():
        myorder = Myorder.objects.get(user=request.user,status=False)
    else:
        if not request.path == reverse('Contents:giohang'):
            messages.warning(request, "Mời bạn thêm một sản phẩm bất kì vào giỏ hàng trước khi sửa thông tin")
            return redirect(reverse('Contents:giohang'))
    myorder =Myorder.objects.get(user=request.user,status=False)
    form =CheckoutFrom(request.POST or None)
    if D.exists():
        AC=InfomationUsers.objects.get(user=request.user)
        print("User tồn tại ")
        if request.method =="POST":
            if form.is_valid():
                #self.cleaned_data[‘field’]sẽ tạo ra Lỗi KeyError , trong khi self.cleaned_data.get(‘field’)sẽ trả về Không có .
                # Django sẽ lưu các dữ liệu đã được kiểm tra là hợp lệ trong thuộc tính cleaned_data
                #cleaned_data lấy thông tin người dùng nhập ra để kiểm tra
                adress=form.cleaned_data.get('adress')
                phone=form.cleaned_data.get('phone')
                gender=form.cleaned_data.get('gender')
                bridday=form.cleaned_data.get('bridday')
                identify=form.cleaned_data.get('identify')
                addinfousers=InfomationUsers(
                #dữ liệu người dùng nhập vào phải gán chó nó bằng với thuộc tính trong model thì mới hiển thị lên database
                    user=request.user,
                    adress=adress,
                    gender=gender,
                    phone=phone,
                    bridday=bridday,
                    identify=identify,
                )
                a=InfomationUsers.objects.filter(user=request.user)
                H=Address.objects.filter(user=request.user,address=adress)
                if H.exists():
                    H.delete()
                    addaddress=Address(
                        #dữ liệu người dùng nhập vào phải gán chó nó bằng với thuộc tính trong model thì mới hiển thị lên database
                        user=request.user,
                        address=adress,
                    )
                    addaddress.save()
                    # print("có")
                else:
                    print("lalalalala")
                    addaddress=Address(
                        #dữ liệu người dùng nhập vào phải gán chó nó bằng với thuộc tính trong model thì mới hiển thị lên database
                        user=request.user,
                        address=adress,
                    )
                    addaddress.save()
                if a.exists():
                    a.delete()
                    addinfousers.save()
                    messages.success(request, "Bạn đã cập nhập Thông thành công ")
                    myorder.InfomationUsers=addinfousers
                    myorder.save()
                else:
                    addaddress.save()
                    addinfousers.save()
                    messages.success(request, "Bạn đã thêm thông tin thành công")
                    myorder.InfomationUsers=addinfousers
                    myorder.save()
                return redirect("Contents:profile")
    else:
        if request.method =="POST":
            if form.is_valid():
                adress=form.cleaned_data.get('adress')
                phone=form.cleaned_data.get('phone')
                gender=form.cleaned_data.get('gender')
                bridday=form.cleaned_data.get('bridday')
                identify=form.cleaned_data.get('identify')
                addinfousers=InfomationUsers(
                    user=request.user,
                    adress=adress,
                    gender=gender,
                    phone=phone,
                    bridday=bridday,
                    identify=identify,
                )
                a=InfomationUsers.objects.filter(user=request.user)
                H=Address.objects.filter(user=request.user,address=adress)
                if H.exists():
                    print("có")
                else:
                    print("lalalalala")
                    addaddress=Address(
                        user=request.user,
                        address=adress,
                    )
                    addaddress.save()

                if a.exists():
                    a.delete()
                    addinfousers.save()
                    messages.success(request, "Bạn đã cập nhập Thông thành công ")
                    myorder.InfomationUsers=addinfousers
                    myorder.save()
                else:
                    addinfousers.save()
                    messages.success(request, "Bạn đã thêm thông tin thành công")
                    myorder.InfomationUsers=addinfousers
                    myorder.save()
                return redirect("Contents:profile") 
    return render(request, 'Contents/profile.html',{'form':form,'myorder': myorder})
def donmua(request):
    myorder=Order.objects.filter(user=request.user,status=True)
    myorder2=Order.objects.filter(user=request.user,status=True)
    address=Address.objects.filter(user=request.user)
    total=0
    total1=0
    for i in myorder2:
        total1=i.number * i.product.price
        total=total+total1
    a=InfomationUsers.objects.filter(user=request.user)
    if a.exists():
        queryset=InfomationUsers.objects.get(user=request.user)
    else:
        return render(request, 'Contents/donmua.html')
    print(total)
    myorderproduct=Myorder.objects.filter(user=request.user,status=True)
    context = {
        'myorder': myorder,
        'myorder1':myorder2,
        'Adress':queryset,
        'total':total,
        'address':address,
        'myorderproduct':myorderproduct
    }
    return render(request, 'Contents/donmua.html',context)
def chitietdonmua(request,pk):
    myordertotal = get_object_or_404(Myorder,pk=pk,status=True,user=request.user)
    total=0
    total1=0
    a= myordertotal.products.all()
    for i in a:
        total =i.number * i.product.price
        total1=total1+total
    myorder=Order.objects.filter(user=request.user,status=True)
    myorder2=Order.objects.filter(user=request.user,status=True)
    a=InfomationUsers.objects.filter(user=request.user)
    if a.exists():
        queryset=InfomationUsers.objects.get(user=request.user)
    else:
        return render(request, 'Contents/chitietdonmua.html')
    myorderproduct=Myorder.objects.filter(user=request.user,status=True)
    context = {
        'myorder': myorder,
        'myorder1':myorder2,
        'Adress':queryset,
        'total':total,
        'total1':total1,
        'myordertotal':myordertotal,
        'myorderdetail':a,
        'myorderproduct':myorderproduct
    }
    return render(request, 'Contents/chitietdonmua.html',context)
@login_required
def ProductDetail(request,slug):
   product = get_object_or_404(Product,slug=slug)
   a=Myorder.objects.filter(user=request.user,status=False)
   b=ChooseSizeColor.objects.filter(user=request.user,Product__slug=product.slug)  
   form =Choosesize()
   if request.method =="POST":
       form =Choosesize(request.POST or None)
       print(request.POST)
       if form.is_valid():
           productsize=form.cleaned_data.get('productsize')
           productColor=form.cleaned_data.get('producColor')
           addsize=ChooseSizeColor(
               user=request.user,
               producsize=productsize,
               producColor=productColor,
               Product=product
           )
           if b.exists():
            #    b.delete()
               addsize.save()
            #    b = ChooseSizeColor.objects.get(user=request.user,Product__slug=product.slug)
           else:
               addsize.save()
            #    b = ChooseSizeColor.objects.get(user=request.user,Product__slug=product.slug)

   return render(request, "Contents/productdetails.html", {"productdetail": product, "forms": form})# đưa cái posts và form vào trong đường dẫn blog/post.html
def Themdiachi (request):
    form =AddressForm(request.POST, request.FILES or None)
    print(request.POST)       
    if request.method =="POST":
        if form.is_valid():
            address=form.cleaned_data.get('address')
            addaddress=Address(
                user=request.user,
                address=address,
            )
            addaddress.save()
            messages.success(request, "Bạn đã thêm thông tin địa chỉ thành công")
            return redirect("Contents:Address")
    return render(request, 'Contents/themdiachi.html',{'form':form})
@login_required
def xoasanphamgiohang(request,id):
    #product = get_object_or_404(Product,slug=slug)#ở thư mục urls post path
    queryset=Myorder.objects.filter(user=request.user)#Find all the groups with a member whose name starts with "user"
    c12=Myorder.objects.all()
    #b=ChooseSizeColor.objects.filter(user=request.user,Product__slug=product.slug)
    order=Order.objects.get(id=id)
    #.objects.filter(b__c__name='some name')
   
    #if b.exists():
    print(order.choosesizecolor.producColor)
    print(order.choosesizecolor.producsize)
    print(order.product)
    C=ChooseSizeColor.objects.get(user=request.user,Product=order.product,status=False,producColor=order.choosesizecolor.producColor,producsize=order.choosesizecolor.producsize)
    C.delete()
    #else:
    #   C=""
    #for i in order:
    #    i.delete()
    #C.delete()
    order.delete()

    # D1=Order.objects.get(user=request.user,pk=pk)
    # D1.delete()
    # if queryset.exists():
    #     myorder=queryset[0]
    #     print(myorder)
    #     Myorder_product = Order.objects.filter(
    #         product=order.product,
    #         user=request.user,
    #         status=False,
    #     )#[0]
    #     Myorder_product.delete()
    #     return redirect("Contents:giohang")
    # else:
    #     return redirect("Contents:giohang")
    return redirect("Contents:giohang")
@login_required
def huydonhang(request,pk):
    myordertotal = get_object_or_404(Myorder,pk=pk,status=True,user=request.user)
    b=Payment.objects.filter(user=request.user)
    C=Order.objects.filter(user=request.user)
    myorder=Myorder.objects.filter(pk=pk,status=True,user=request.user)#Find all the groups with a member whose name starts with "user"
    myorder1=Myorder.objects.all()
    k=myordertotal.products.all()
    T=myordertotal.products.all()
    print(myordertotal.Payment)
    if myorder.exists():
        myordertotal.Payment.delete()
        for i in T:
            i.choosesizecolor.delete()
        k.delete()
        myorder.delete()
        messages.success(request, "Bạn đã vừa mới xóa một sản phẩm trong đơn hàng của bạn")
    else:
        messages.success(request, "Không có đon hàng cần xóa")
        return redirect("Contents:donmua")
    return redirect("Contents:donmua")
def danhgiasanpham (request,slug):
   productconsider = get_object_or_404(Product,slug=slug)#ở thư mục urls post path
   form =Commentform(request.POST,request.FILES or None)# request.POST là khi người dùng nhập vào body nó sẽ đưa lên form
   print(request.POST)
   if request.method =="POST":
       if form.is_valid():
           Content=form.cleaned_data.get('Content')
           Stars=form.cleaned_data.get('Stars')
           #images=request.FILES.getlist("image")
        #    images=request.FILES.getlist("image")
           images =request.FILES.get('image')
           comemnt=Comment(
                ProductComemnt=productconsider,
                writer=request.user,
                Content=Content,
                Stars=Stars,
                image=images,
            )
           comemnt.save()
   return render(request, "Contents/danhgiasanpham.html", {"Considerproduct": productconsider, "forms": form})
