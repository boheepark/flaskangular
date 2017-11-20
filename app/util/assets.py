from flask_assets import Bundle

bundles = {
    "modules_js": Bundle(
        "node_modules/angular/angular.min.js",
        "node_modules/angular-messages/angular-messages.min.js",
        "node_modules/angular-route/angular-route.min.js",
        "node_modules/jquery/dist/jquery.min.js",
        "node_modules/bootstrap/dist/js/bootstrap.min.js",
        output="gen/modules.js",
        filters="jsmin"),
    "modules_css": Bundle(
        "node_modules/bootstrap/dist/css/bootstrap.min.css",
        "node_modules/font-awesome/css/font-awesome.min.css",
        output="gen/modules.css",
        filters="cssmin"),
    # "app_js": Bundle(
    #     "app.js",
    #     output="gen/app.js",
    #     filters="jsmin"),
    "app_css": Bundle(
        "css/auth.css",
        "css/styles.css",
        output="gen/app.css",
        filters="cssmin"),
    "base_js": Bundle(
        "base/app.js",
        "base/logo.directive.js",
        output="gen/base.js",
        filters="jsmin"),
    "home_js": Bundle(
        "home/home.controller.js",
        output="gen/home.js",
        filters="jsmin"),
    "auth_js": Bundle(
        "auth/auth.factory.js",
        "auth/auth.controller.js",
        "auth/authBtn.directive.js",
        "auth/bgEffect.component.js",
        "auth/checkDb.directive.js",
        "auth/checkPw.directive.js",
        "auth/compareTo.directive.js",
        output="gen/auth.js",
        filters="jsmin"),
    "users_js": Bundle(
        "users/users.factory.js",
        output="gen/users.js",
        filters="jsmin"),
    "trades_js": Bundle(
        "trades/trades.factory.js",
        "trades/trades.directive.js",
        output="gen/trades.js",
        filters="jsmin")
}