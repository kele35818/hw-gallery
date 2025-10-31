**# 华为云创计划 - 动态云相册 (Python + Flexus + OBS)

本项目为申请 **华为沃土云创计划** 激励而创建的应用演示。

这是一个基于 Python Flask 框架构建的动态云相册应用。它旨在展示如何将华为云的基础设施即服务 (IaaS) 与平台即服务 (PaaS) 相结合，构建一个简单、高效且具备“动静分离”架构的Web应用。

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)
![Huawei Cloud](https://img.shields.io/badge/Huawei_Cloud-Flexus_&_OBS-red.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## 📸 项目特色 (Features)

* **动静分离：** 应用逻辑（Python/Flask）运行在 `Flexus 应用服务器` 上，而所有图片资源则存储在 `OBS 对象存储` 中，降低了服务器带宽压力，提升了加载速度。
* **现代前端：** 使用 CSS3 Flexbox 和 Grid 布局，实现了“高大上”的响应式图片画廊。
* **交互体验：** 包含图片懒加载、悬停放大效果以及点击查看大图 (Lightbox) 功能。
* **轻量高效：** 后端使用 Flask 微框架，代码简洁，部署快速。

---

## 🛠️ 技术栈 (Technology Stack)

* **后端 (Backend):** Python 3, Flask
* **前端 (Frontend):** HTML5, CSS3, JavaScript (ES6+)
* **云服务 (Cloud Services):**
    * `华为云 Flexus 应用服务器`: 托管和运行 Flask Web 应用。
    * `华为云 OBS 对象存储`: 存储和分发所有相册图片。

---

## 🚀 快速开始 (Getting Started)

### 先决条件

* Python 3.x
* 已开通的华为云 Flexus 服务器 (已开放 5000 端口)
* 已创建并设为“公共读”的华为云 OBS 桶

### 克隆项目

```bash
git clone [你的项目Git地址]
cd [你的项目目录]**

