# <!-- 
#     <center>

        
#         <form action="" method="POST" enctype="multipart/form-data">
#             {% csrf_token %}
            
#             <label for="">Pname</label>
#             <input type="text" name="pname"> <br>
            
#             <label for="">pdesc</label>
#             <input type="text" name="pdesc"> <br>
            
#             <label for="">Price</label>
#             <input type="text" name="price"> <br>
            
#             <label for="">category</label>
#             <input type="text" name="category"> <br>
            
#             <label for="">add Image</label>
#             <input type="file" name="img_data" >  <br>
            
#             <input type="submit">
            
#         </form>
        
#     </center> -->


#     if request.method == 'POST':
#         pname=request.POST['pname']
#         pdesc=request.POST['pdesc']
#         price=request.POST['price']
#         pcategory=request.POST['category']
#         img_data=request.FILES['img_data']
#         Products.objects.create(pname=pname,
#                                 pdesc=pdesc,
#                                 price=price,
#                                 pcategory=pcategory,
#                                 pimages=img_data)

