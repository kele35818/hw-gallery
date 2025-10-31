from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def gallery():
    # 你的OBS图片地址列表
    image_urls = [
        "https://hwsg-kele.obs.ap-southeast-3.myhuaweicloud.com/IMG/pexels-cottonbro-6853297.jpg",
        "https://hwsg-kele.obs.ap-southeast-3.myhuaweicloud.com/IMG/pexels-georgi-kanov-442883099-20341423.jpg",
        "https://hwsg-kele.obs.ap-southeast-3.myhuaweicloud.com/IMG/pexels-ian-panelo-17988001.jpg",
        "https://hwsg-kele.obs.ap-southeast-3.myhuaweicloud.com/IMG/pexels-kirsten-buhne-682055-2261566.jpg",
        "https://hwsg-kele.obs.ap-southeast-3.myhuaweicloud.com/IMG/pexels-kowalievska-1416792.jpg",
        "https://hwsg-kele.obs.ap-southeast-3.myhuaweicloud.com/IMG/pexels-meriem-a-2149355236-34494110.jpg",
        "https://hwsg-kele.obs.ap-southeast-3.myhuaweicloud.com/IMG/pexels-neamt-victor-34807113-26152822.jpg",
        "https://hwsg-kele.obs.ap-southeast-3.myhuaweicloud.com/IMG/pexels-serdar-tas-14373165-34507438.jpg",
        "https://hwsg-kele.obs.ap-southeast-3.myhuaweicloud.com/IMG/pexels-thirdman-8942607.jpg"
    ]
    return render_template('index.html', images=image_urls)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
