import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryPopuOfScience(params) {
  return request('/api/xadmin/v1/popu_of_science', {
    params,
  });
}
export async function removePopuOfScience(params) {
  return request(`/api/xadmin/v1/popu_of_science/${params}`, {
    method: 'DELETE',
  });
}
export async function addPopuOfScience(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/popu_of_science', {
    method: 'POST',
    data: fileData,
  });
}
export async function updatePopuOfScience(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/popu_of_science/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryPopuOfScienceVerboseName(params) {
  return request('/api/xadmin/v1/popu_of_science/verbose_name', {
    params,
  });
}
export async function queryPopuOfScienceListDisplay(params) {
  return request('/api/xadmin/v1/popu_of_science/list_display', {
    params,
  });
}
export async function queryPopuOfScienceDisplayOrder(params) {
  return request('/api/xadmin/v1/popu_of_science/display_order', {
    params,
  });
}


