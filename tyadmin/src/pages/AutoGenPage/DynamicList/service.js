import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryDynamic(params) {
  return request('/api/xadmin/v1/dynamic', {
    params,
  });
}
export async function removeDynamic(params) {
  return request(`/api/xadmin/v1/dynamic/${params}`, {
    method: 'DELETE',
  });
}
export async function addDynamic(params) {
  let fileFieldList = ["dynamicPicture"]
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/dynamic', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateDynamic(params, id) {
  let fileFieldList = ["dynamicPicture"]
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/dynamic/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryDynamicVerboseName(params) {
  return request('/api/xadmin/v1/dynamic/verbose_name', {
    params,
  });
}
export async function queryDynamicListDisplay(params) {
  return request('/api/xadmin/v1/dynamic/list_display', {
    params,
  });
}
export async function queryDynamicDisplayOrder(params) {
  return request('/api/xadmin/v1/dynamic/display_order', {
    params,
  });
}


