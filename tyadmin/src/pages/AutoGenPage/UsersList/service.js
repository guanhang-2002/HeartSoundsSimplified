import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryUsers(params) {
  return request('/api/xadmin/v1/users', {
    params,
  });
}
export async function removeUsers(params) {
  return request(`/api/xadmin/v1/users/${params}`, {
    method: 'DELETE',
  });
}
export async function addUsers(params) {
  let fileFieldList = ["photo"]
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/users', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateUsers(params, id) {
  let fileFieldList = ["photo"]
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/users/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryUsersVerboseName(params) {
  return request('/api/xadmin/v1/users/verbose_name', {
    params,
  });
}
export async function queryUsersListDisplay(params) {
  return request('/api/xadmin/v1/users/list_display', {
    params,
  });
}
export async function queryUsersDisplayOrder(params) {
  return request('/api/xadmin/v1/users/display_order', {
    params,
  });
}

export async function updateUserPassword(params) {
    return request('/api/xadmin/v1/list_change_password', {
     method: 'POST',
     data: { ...params},
});
}

