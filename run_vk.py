import vk_api
from auth_data import group_access_token as group_token


vk = vk_api.VkApi(token=group_token)
vk._auth_token()

uploader = vk_api.upload.VkUpload(vk)
