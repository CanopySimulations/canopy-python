# coding: utf-8

"""
    Canopy.Api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from canopy.openapi.api_client import ApiClient
from canopy.openapi.exceptions import (
    ApiTypeError,
    ApiValueError
)


class SimVersionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def sim_version_get_document(self, sim_version, document_path, **kwargs):  # noqa: E501
        """sim_version_get_document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sim_version_get_document(sim_version, document_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str sim_version: (required)
        :param str document_path: (required)
        :param str tenant_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetSimVersionDocumentQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.sim_version_get_document_with_http_info(sim_version, document_path, **kwargs)  # noqa: E501

    def sim_version_get_document_with_http_info(self, sim_version, document_path, **kwargs):  # noqa: E501
        """sim_version_get_document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sim_version_get_document_with_http_info(sim_version, document_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str sim_version: (required)
        :param str document_path: (required)
        :param str tenant_id:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetSimVersionDocumentQueryResult, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['sim_version', 'document_path', 'tenant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sim_version_get_document" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'sim_version' is set
        if self.api_client.client_side_validation and ('sim_version' not in local_var_params or  # noqa: E501
                                                        local_var_params['sim_version'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sim_version` when calling `sim_version_get_document`")  # noqa: E501
        # verify the required parameter 'document_path' is set
        if self.api_client.client_side_validation and ('document_path' not in local_var_params or  # noqa: E501
                                                        local_var_params['document_path'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `document_path` when calling `sim_version_get_document`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sim_version' in local_var_params:
            path_params['simVersion'] = local_var_params['sim_version']  # noqa: E501
        if 'document_path' in local_var_params:
            path_params['documentPath'] = local_var_params['document_path']  # noqa: E501

        query_params = []
        if 'tenant_id' in local_var_params and local_var_params['tenant_id'] is not None:  # noqa: E501
            query_params.append(('tenantId', local_var_params['tenant_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/sim-versions/{simVersion}/documents/{documentPath}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSimVersionDocumentQueryResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sim_version_get_documents(self, sim_version, **kwargs):  # noqa: E501
        """sim_version_get_documents  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sim_version_get_documents(sim_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str sim_version: (required)
        :param str tenant_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetSimVersionDocumentsQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.sim_version_get_documents_with_http_info(sim_version, **kwargs)  # noqa: E501

    def sim_version_get_documents_with_http_info(self, sim_version, **kwargs):  # noqa: E501
        """sim_version_get_documents  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sim_version_get_documents_with_http_info(sim_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str sim_version: (required)
        :param str tenant_id:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetSimVersionDocumentsQueryResult, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['sim_version', 'tenant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sim_version_get_documents" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'sim_version' is set
        if self.api_client.client_side_validation and ('sim_version' not in local_var_params or  # noqa: E501
                                                        local_var_params['sim_version'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sim_version` when calling `sim_version_get_documents`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sim_version' in local_var_params:
            path_params['simVersion'] = local_var_params['sim_version']  # noqa: E501

        query_params = []
        if 'tenant_id' in local_var_params and local_var_params['tenant_id'] is not None:  # noqa: E501
            query_params.append(('tenantId', local_var_params['tenant_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/sim-versions/{simVersion}/documents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSimVersionDocumentsQueryResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sim_version_get_downloads(self, sim_version, **kwargs):  # noqa: E501
        """sim_version_get_downloads  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sim_version_get_downloads(sim_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str sim_version: (required)
        :param str tenant_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetSimVersionDownloadsQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.sim_version_get_downloads_with_http_info(sim_version, **kwargs)  # noqa: E501

    def sim_version_get_downloads_with_http_info(self, sim_version, **kwargs):  # noqa: E501
        """sim_version_get_downloads  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sim_version_get_downloads_with_http_info(sim_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str sim_version: (required)
        :param str tenant_id:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetSimVersionDownloadsQueryResult, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['sim_version', 'tenant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sim_version_get_downloads" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'sim_version' is set
        if self.api_client.client_side_validation and ('sim_version' not in local_var_params or  # noqa: E501
                                                        local_var_params['sim_version'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sim_version` when calling `sim_version_get_downloads`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sim_version' in local_var_params:
            path_params['simVersion'] = local_var_params['sim_version']  # noqa: E501

        query_params = []
        if 'tenant_id' in local_var_params and local_var_params['tenant_id'] is not None:  # noqa: E501
            query_params.append(('tenantId', local_var_params['tenant_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/sim-versions/{simVersion}/downloads', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSimVersionDownloadsQueryResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sim_version_get_sim_version(self, **kwargs):  # noqa: E501
        """sim_version_get_sim_version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sim_version_get_sim_version(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tenant_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.sim_version_get_sim_version_with_http_info(**kwargs)  # noqa: E501

    def sim_version_get_sim_version_with_http_info(self, **kwargs):  # noqa: E501
        """sim_version_get_sim_version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sim_version_get_sim_version_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tenant_id:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['tenant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sim_version_get_sim_version" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'tenant_id' in local_var_params and local_var_params['tenant_id'] is not None:  # noqa: E501
            query_params.append(('tenantId', local_var_params['tenant_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/sim-versions/current', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sim_version_get_wiki_document(self, wiki_version, document_path, **kwargs):  # noqa: E501
        """sim_version_get_wiki_document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sim_version_get_wiki_document(wiki_version, document_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str wiki_version: (required)
        :param str document_path: (required)
        :param str tenant_id:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetWikiDocumentQueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.sim_version_get_wiki_document_with_http_info(wiki_version, document_path, **kwargs)  # noqa: E501

    def sim_version_get_wiki_document_with_http_info(self, wiki_version, document_path, **kwargs):  # noqa: E501
        """sim_version_get_wiki_document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sim_version_get_wiki_document_with_http_info(wiki_version, document_path, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str wiki_version: (required)
        :param str document_path: (required)
        :param str tenant_id:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetWikiDocumentQueryResult, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['wiki_version', 'document_path', 'tenant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sim_version_get_wiki_document" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'wiki_version' is set
        if self.api_client.client_side_validation and ('wiki_version' not in local_var_params or  # noqa: E501
                                                        local_var_params['wiki_version'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `wiki_version` when calling `sim_version_get_wiki_document`")  # noqa: E501
        # verify the required parameter 'document_path' is set
        if self.api_client.client_side_validation and ('document_path' not in local_var_params or  # noqa: E501
                                                        local_var_params['document_path'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `document_path` when calling `sim_version_get_wiki_document`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'wiki_version' in local_var_params:
            path_params['wikiVersion'] = local_var_params['wiki_version']  # noqa: E501
        if 'document_path' in local_var_params:
            path_params['documentPath'] = local_var_params['document_path']  # noqa: E501

        query_params = []
        if 'tenant_id' in local_var_params and local_var_params['tenant_id'] is not None:  # noqa: E501
            query_params.append(('tenantId', local_var_params['tenant_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/sim-versions/{wikiVersion}/wiki/{documentPath}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetWikiDocumentQueryResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sim_version_post_sim_version(self, sim_version_data, **kwargs):  # noqa: E501
        """sim_version_post_sim_version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sim_version_post_sim_version(sim_version_data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param NewSimVersionData sim_version_data: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.sim_version_post_sim_version_with_http_info(sim_version_data, **kwargs)  # noqa: E501

    def sim_version_post_sim_version_with_http_info(self, sim_version_data, **kwargs):  # noqa: E501
        """sim_version_post_sim_version  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sim_version_post_sim_version_with_http_info(sim_version_data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param NewSimVersionData sim_version_data: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['sim_version_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sim_version_post_sim_version" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'sim_version_data' is set
        if self.api_client.client_side_validation and ('sim_version_data' not in local_var_params or  # noqa: E501
                                                        local_var_params['sim_version_data'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `sim_version_data` when calling `sim_version_post_sim_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'sim_version_data' in local_var_params:
            body_params = local_var_params['sim_version_data']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/sim-versions/current', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)