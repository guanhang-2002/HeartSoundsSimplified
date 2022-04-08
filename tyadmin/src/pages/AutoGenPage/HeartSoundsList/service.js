import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryHeartSounds(params) {
  return request('/api/xadmin/v1/heart_sounds', {
    params,
  });
}
export async function removeHeartSounds(params) {
  return request(`/api/xadmin/v1/heart_sounds/${params}`, {
    method: 'DELETE',
  });
}
export async function addHeartSounds(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/heart_sounds', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateHeartSounds(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/heart_sounds/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryHeartSoundsVerboseName(params) {
  return request('/api/xadmin/v1/heart_sounds/verbose_name', {
    params,
  });
}
export async function queryHeartSoundsListDisplay(params) {
  return request('/api/xadmin/v1/heart_sounds/list_display', {
    params,
  });
}
export async function queryHeartSoundsDisplayOrder(params) {
  return request('/api/xadmin/v1/heart_sounds/display_order', {
    params,
  });
}


