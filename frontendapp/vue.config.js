module.exports = {
    devServer: {
        disableHostCheck: true,
        proxy: {
            "/api": {
                target: "http://127.0.0.1:8000",
                secure: false,
                changeOrigin: true
            },
            "/admin": {
                target: "http://127.0.0.1:8000",
                secure: false,
                changeOrigin: true
            },
            "/media":{
                target: "http://127.0.0.1:8000",
                secure: false,
                changeOrigin: true
            }
        }
    },
}