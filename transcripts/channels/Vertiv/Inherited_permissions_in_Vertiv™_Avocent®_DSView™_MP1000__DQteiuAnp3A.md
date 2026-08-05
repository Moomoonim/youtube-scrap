# Inherited permissions in Vertiv™ Avocent® DSView™ MP1000

- 영상 링크: https://www.youtube.com/watch?v=DQteiuAnp3A
- 채널: Vertiv
- 업로드일: 2025-11-06
- 자막 언어: en
- 단어 수: 약 220개

---

## 스크립트

This video will cover the Verdive DSV solution MP-1000 inherited permissions. Inherited permissions refer to the way user access rights and roles are automatically passed down from higher level configurations such as system roles, resource groups, or mapped user groups to individual users or devices. These permissions are not manually assigned to the user directly but are inherited from the group or role that they belong to. This allows for scalable and consistent access control across the platform. When a user is created or mapped to the management platform, they'll need to be assigned a system role to define what actions the user can perform. The user will also need to be assigned a resource group to define which devices or targets the user can access. Once added to that role or group, the user will inherit the permissions associated with it. If a new device is added to the resource group that a user has access to, the user will now have access to the new device. Once a user is assigned to a system role, they should automatically gain access to the corresponding devices. If the user is removed from the role, those permissions are revoked and they no longer have access. When a device is unenrolled and then reenrolled, the inherited roles and mappings will be reapplied.
