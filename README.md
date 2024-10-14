This repository contains first Django projects.
## Permissions Setup

### Groups:
- **Viewers**: Can only view posts.
- **Editors**: Can view, create, and edit posts.
- **Admins**: Can view, create, edit, and delete posts.

### Custom Permissions:
- `can_view`: Allows viewing of posts.
- `can_create`: Allows creation of posts.
- `can_edit`: Allows editing of posts.
- `can_delete`: Allows deletion of posts.

### Views:
- The `post_list` view requires the `can_view` permission.
- The `post_create` view requires the `can_create` permission.
- The `post_edit` view requires the `can_edit` permission.
- The `post_delete` view requires the `can_delete` permission.
