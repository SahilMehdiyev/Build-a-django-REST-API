from rest_framework import permissions



class IsStaffEditorPermission(permissions.DjangoObjectPermissions):
    def has_permission(self, request, view):
        user=request.user
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm('products.view_product'):
                return True
            return False
        return False
    
