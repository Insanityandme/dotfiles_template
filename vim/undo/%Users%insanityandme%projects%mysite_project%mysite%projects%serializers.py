Vim�UnDo� '��%U�����&���VPٻ�3�:b֜>n                    7       7   7   7    W��_   # _�                    	       ����                                                                                                                                                                                                                                                                                                                                                             W���    �      
         #        return object.thumbnail.url5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W���    �                       fields = '__all__'5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W���   	 �                       exclude = ('content')5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                             W��!     �      	         &    def get_thumbnail_url(self, item):5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             W��$    �      
         !        return item.thumbnail.url5�_�                          ����                                                                                                                                                                                                                                                                                                                            	                    V       W���     �                %    def get_thumbnail_url(self, obj):            return obj.thumbnail.url5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       W���     �               �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       W���     �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       W���    �                 5�_�                          ����                                                                                                                                                                                                                                                                                                                                                V       W���     �               7    thumbnail_url = serializers.SerializerMethodField()5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       W���    �               %    def get_thumbnail_url(self, obj):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       W���     �                          return obj.thumbnail.url5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       W���     �                 (        return "%s%s" (obj.thumbnail.url5�_�                       ;    ����                                                                                                                                                                                                                                                                                                                                                V       W���     �                 ;        return "%s%s" ("localhost:8080" + obj.thumbnail.url5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       W���    �                 <        return "%s%s" ("localhost:8080" + obj.thumbnail.url)5�_�      %                  +    ����                                                                                                                                                                                                                                                                                                                                                V       W���    �                 >        return "%s%s" % ("localhost:8080" + obj.thumbnail.url)5�_�       &   !       %      <    ����                                                                                                                                                                                                                                                                                                                                                V       W���    �                     �               5�_�   %   '           &           ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��     �                ,    print(self.context['request'].thumbnail)5�_�   &   (           '           ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��     �             �             5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��    �               ,    print(self.context['request'].thumbnail)5�_�   (   *           )           ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��    �                 5�_�   )   -           *          ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��]    �                0        print(self.context['request'].thumbnail)5�_�   *   0   ,       -      =    ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W���    �                 =        return "%s%s" % ("localhost:8080", obj.thumbnail.url)5�_�   -   1   .       0           ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��     �                �             5�_�   0   2           1      "    ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��     �                     �               5�_�   1   3           2          ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��     �                A        return HttpRequest.build_absolute_uri(self.thumbnail.url)5�_�   2   4           3      >    ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��"    �                 M        return self.context['request'].build_absolute_uri(self.thumbnail.url)5�_�   3   6           4      <    ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��-     �                     �               5�_�   4   7   5       6          ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��[     �                @        return HttpRequest.build_absolute_uri(obj.thumbnail.url)5�_�   6               7           ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��^   # �                #from django.http import HttpRequest5�_�   4           6   5          ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��7    �               N        # return self.context['request'].build_absolute_uri(obj.thumbnail.url)5�_�   -   /       0   .      $    ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��1     �                J        return self.context['view'].build_absolute_uri(self.thumbnail.url)5�_�   .               /      #    ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W��4    �                R        return self.context['view'].request.build_absolute_uri(self.thumbnail.url)5�_�   *       +   -   ,      <    ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W���    �                J        return "%s%s" % ("localhost:8080", obj.thumbnail.get_absolute_url)5�_�   *           ,   +      <    ����                                                                                                                                                                                                                                                                                                                               +          +       V   +    W���    �                9        return "%s%s" % ("localhost:8080", obj.thumbnail)5�_�       "       %   !      =    ����                                                                                                                                                                                                                                                                                                                                                V       W��j     �                '        return self.context['request'].5�_�   !   #           "      '    ����                                                                                                                                                                                                                                                                                                                                                V       W��y     �                        return 5�_�   "   $           #          ����                                                                                                                                                                                                                                                                                                                                                V       W��|     �                       �               %        url = self.context['request']5�_�   #               $      %    ����                                                                                                                                                                                                                                                                                                                                                V       W���     �               &        url = self.context['request'].5�_�                          ����                                                                                                                                                                                                                                                                                                                                                V       W���     �               3    thumbnail = serializers.SerializerMethodField()5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       W���    �                        return obj.category5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W���     �               3    thumbnail = serializers.SerializerMethodField()5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             W�{�    �                '#from rest_framework import serializers5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             W�{�     �                (# from rest_framework import serializers5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             W�{�     �               3#class ItemSerializer(serializers.ModelSerializer):5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             W�{�     �                5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             W�{�     �               2class ItemSerializer(serializers.ModelSerializer):5�_�                            ����                                                                                                                                                                                                                                                                                                                                                          W�{�    �               4# class ItemSerializer(serializers.ModelSerializer):�             	   9#     thumbnail_url = serializers.SerializerMethodField()   #    (#     def get_thumbnail_url(self, item):   %#         return object.thumbnail.url   #    #     class Meta:   #         model = Item   #         fields = '__all__'   #         depth = 25�_�                           ����                                                                                                                                                                                                                                                                                                                                                          W�{�     �               #5�_�      	              
       ����                                                                                                                                                                                                                                                                                                                                                          W�{�    �   	            #5�_�      
           	   
        ����                                                                                                                                                                                                                                                                                                                                                          W�{�     �   	           5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                          W�{�    �              5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                          W�|     �                5�_�                            ����                                                                                                                                                                                                                                                                                                                                                          W��
     �                ' from rest_framework import serializers5�_�                             ����                                                                                                                                                                                                                                                                                                                                                          W��
     �                &from rest_framework import serializers5��