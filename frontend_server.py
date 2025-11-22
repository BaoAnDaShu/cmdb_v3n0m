#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
前端静态文件服务器
配置CORS支持，允许前端访问Django API
"""

import http.server
import socketserver
import os
from http.server import SimpleHTTPRequestHandler

# 自定义请求处理器，添加CORS支持
class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # 添加CORS头信息
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        super().end_headers()
    
    def do_OPTIONS(self):
        # 处理预检请求
        self.send_response(200)
        self.end_headers()

# 设置服务器配置
PORT = 8080
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), 'frontend')

# 切换到前端目录
os.chdir(FRONTEND_DIR)

# 创建服务器
httpd = socketserver.TCPServer(("", PORT), CORSRequestHandler)
print(f"前端服务器已启动")
print(f"服务地址: http://localhost:{PORT}")
print(f"服务目录: {FRONTEND_DIR}")
print("按 Ctrl+C 停止服务器")
try:
    # 启动服务器
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\n服务器已停止")