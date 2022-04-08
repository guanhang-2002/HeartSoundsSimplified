import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryIntroduce(params) {
  return request('/api/xadmin/v1/introduce', {
    params,
  });
}
export async function removeIntroduce(params) {
  return request(`/api/xadmin/v1/introduce/${params}`, {
    method: 'DELETE',
  });
}
export async function addIntroduce(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/introduce', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateIntroduce(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/introduce/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryIntroduceVerboseName(params) {
  return request('/api/xadmin/v1/introduce/verbose_name', {
    params,
  });
}
export async function queryIntroduceListDisplay(params) {
  return request('/api/xadmin/v1/introduce/list_display', {
    params,
  });
}
export async function queryIntroduceDisplayOrder(params) {
  return request('/api/xadmin/v1/introduce/display_order', {
    params,
  });
}


