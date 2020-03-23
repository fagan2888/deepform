# coding: utf-8

"""
    OPIF Manager API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DownloadApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def download_folder_id_file_manager_id_pdf_get(self, folder_id, file_manager_id, **kwargs):  # noqa: E501
        """Dowload converted File  # noqa: E501

        Downloads a converted File based on Folder ID and File Manager ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_folder_id_file_manager_id_pdf_get(folder_id, file_manager_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_id: Folder ID (required)
        :param str file_manager_id: File Manager ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_folder_id_file_manager_id_pdf_get_with_http_info(folder_id, file_manager_id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_folder_id_file_manager_id_pdf_get_with_http_info(folder_id, file_manager_id, **kwargs)  # noqa: E501
            return data

    def download_folder_id_file_manager_id_pdf_get_with_http_info(self, folder_id, file_manager_id, **kwargs):  # noqa: E501
        """Dowload converted File  # noqa: E501

        Downloads a converted File based on Folder ID and File Manager ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_folder_id_file_manager_id_pdf_get_with_http_info(folder_id, file_manager_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str folder_id: Folder ID (required)
        :param str file_manager_id: File Manager ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['folder_id', 'file_manager_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_folder_id_file_manager_id_pdf_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'folder_id' is set
        if ('folder_id' not in params or
                params['folder_id'] is None):
            raise ValueError("Missing the required parameter `folder_id` when calling `download_folder_id_file_manager_id_pdf_get`")  # noqa: E501
        # verify the required parameter 'file_manager_id' is set
        if ('file_manager_id' not in params or
                params['file_manager_id'] is None):
            raise ValueError("Missing the required parameter `file_manager_id` when calling `download_folder_id_file_manager_id_pdf_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'folder_id' in params:
            path_params['folderID'] = params['folder_id']  # noqa: E501
        if 'file_manager_id' in params:
            path_params['fileManagerID'] = params['file_manager_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/download/{folderID}/{fileManagerID}.pdf', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
