<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta name="robots" content="noindex,nofollow" />
        <style>
            /* Copyright (c) 2010, Yahoo! Inc. All rights reserved. Code licensed under the BSD License: http://developer.yahoo.com/yui/license.html */
            html{color:#000;background:#FFF;}body,div,dl,dt,dd,ul,ol,li,h1,h2,h3,h4,h5,h6,pre,code,form,fieldset,legend,input,textarea,p,blockquote,th,td{margin:0;padding:0;}table{border-collapse:collapse;border-spacing:0;}fieldset,img{border:0;}address,caption,cite,code,dfn,em,strong,th,var{font-style:normal;font-weight:normal;}li{list-style:none;}caption,th{text-align:left;}h1,h2,h3,h4,h5,h6{font-size:100%;font-weight:normal;}q:before,q:after{content:'';}abbr,acronym{border:0;font-variant:normal;}sup{vertical-align:text-top;}sub{vertical-align:text-bottom;}input,textarea,select{font-family:inherit;font-size:inherit;font-weight:inherit;}input,textarea,select{*font-size:100%;}legend{color:#000;}

            html { background: #eee; padding: 10px }
            img { border: 0; }
            #sf-resetcontent { width:970px; margin:0 auto; }
                        .sf-reset { font: 11px Verdana, Arial, sans-serif; color: #333 }
            .sf-reset .clear { clear:both; height:0; font-size:0; line-height:0; }
            .sf-reset .clear_fix:after { display:block; height:0; clear:both; visibility:hidden; }
            .sf-reset .clear_fix { display:inline-block; }
            .sf-reset * html .clear_fix { height:1%; }
            .sf-reset .clear_fix { display:block; }
            .sf-reset, .sf-reset .block { margin: auto }
            .sf-reset abbr { border-bottom: 1px dotted #000; cursor: help; }
            .sf-reset p { font-size:14px; line-height:20px; color:#868686; padding-bottom:20px }
            .sf-reset strong { font-weight:bold; }
            .sf-reset a { color:#6c6159; cursor: default; }
            .sf-reset a img { border:none; }
            .sf-reset a:hover { text-decoration:underline; }
            .sf-reset em { font-style:italic; }
            .sf-reset h1, .sf-reset h2 { font: 20px Georgia, "Times New Roman", Times, serif }
            .sf-reset .exception_counter { background-color: #fff; color: #333; padding: 6px; float: left; margin-right: 10px; float: left; display: block; }
            .sf-reset .exception_title { margin-left: 3em; margin-bottom: 0.7em; display: block; }
            .sf-reset .exception_message { margin-left: 3em; display: block; }
            .sf-reset .traces li { font-size:12px; padding: 2px 4px; list-style-type:decimal; margin-left:20px; }
            .sf-reset .block { background-color:#FFFFFF; padding:10px 28px; margin-bottom:20px;
                border-bottom-right-radius: 16px;
                border-bottom-left-radius: 16px;
                border-bottom:1px solid #ccc;
                border-right:1px solid #ccc;
                border-left:1px solid #ccc;
                word-wrap: break-word;
            }
            .sf-reset .block_exception { background-color:#ddd; color: #333; padding:20px;
                border-top-left-radius: 16px;
                border-top-right-radius: 16px;
                border-top:1px solid #ccc;
                border-right:1px solid #ccc;
                border-left:1px solid #ccc;
                overflow: hidden;
                word-wrap: break-word;
            }
            .sf-reset a { background:none; color:#868686; text-decoration:none; }
            .sf-reset a:hover { background:none; color:#313131; text-decoration:underline; }
            .sf-reset ol { padding: 10px 0; }
            .sf-reset h1 { background-color:#FFFFFF; padding: 15px 28px; margin-bottom: 20px;
                border-radius: 10px;
                border: 1px solid #ccc;
            }
        </style>
    </head>
    <body ondblclick="var t = event.target; if (t.title && !t.href) { var f = t.innerHTML; t.innerHTML = t.title; t.title = f; }">
                    <div id="sf-resetcontent" class="sf-reset">
                <h1>Whoops, looks like something went wrong.</h1>
                                        <h2 class="block_exception clear_fix">
                            <span class="exception_counter">1/1</span>
                            <span class="exception_title"><abbr title="ErrorException">ErrorException</abbr> in <a title="/home/pi/test/app/Http/Controllers/RackController.php line 81">RackController.php line 81</a>:</span>
                            <span class="exception_message">Undefined index: rack</span>
                        </h2>
                        <div class="block">
                            <ol class="traces list_exception">
       <li> in <a title="/home/pi/test/app/Http/Controllers/RackController.php line 81">RackController.php line 81</a></li>
       <li>at <abbr title="Illuminate\Foundation\Bootstrap\HandleExceptions">HandleExceptions</abbr>->handleError(8, 'Undefined index: rack', '/home/pi/test/app/Http/Controllers/RackController.php', 81, <em>array</em>('request' => <em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), 'rack' => <em>object</em>(<abbr title="App\Rack">Rack</abbr>), 'data' => <em>array</em>('barcode' => 1231425363543.0, 'rack_id' => 1, 'row' => 4))) in <a title="/home/pi/test/app/Http/Controllers/RackController.php line 81">RackController.php line 81</a></li>
       <li>at <abbr title="App\Http\Controllers\RackController">RackController</abbr>->update(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), <em>object</em>(<abbr title="App\Rack">Rack</abbr>))</li>
       <li>at <abbr title=""></abbr>call_user_func_array(<em>array</em>(<em>object</em>(<abbr title="App\Http\Controllers\RackController">RackController</abbr>), 'update'), <em>array</em>(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), <em>object</em>(<abbr title="App\Rack">Rack</abbr>))) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Controller.php line 55">Controller.php line 55</a></li>
       <li>at <abbr title="Illuminate\Routing\Controller">Controller</abbr>->callAction('update', <em>array</em>(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), <em>object</em>(<abbr title="App\Rack">Rack</abbr>))) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/ControllerDispatcher.php line 44">ControllerDispatcher.php line 44</a></li>
       <li>at <abbr title="Illuminate\Routing\ControllerDispatcher">ControllerDispatcher</abbr>->dispatch(<em>object</em>(<abbr title="Illuminate\Routing\Route">Route</abbr>), <em>object</em>(<abbr title="App\Http\Controllers\RackController">RackController</abbr>), 'update') in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Route.php line 203">Route.php line 203</a></li>
       <li>at <abbr title="Illuminate\Routing\Route">Route</abbr>->runController() in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Route.php line 160">Route.php line 160</a></li>
       <li>at <abbr title="Illuminate\Routing\Route">Route</abbr>->run() in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Router.php line 559">Router.php line 559</a></li>
       <li>at <abbr title="Illuminate\Routing\Router">Router</abbr>->Illuminate\Routing\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Pipeline.php line 30">Pipeline.php line 30</a></li>
       <li>at <abbr title="Illuminate\Routing\Pipeline">Pipeline</abbr>->Illuminate\Routing\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Middleware/SubstituteBindings.php line 41">SubstituteBindings.php line 41</a></li>
       <li>at <abbr title="Illuminate\Routing\Middleware\SubstituteBindings">SubstituteBindings</abbr>->handle(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), <em>object</em>(<abbr title="Closure">Closure</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php line 148">Pipeline.php line 148</a></li>
       <li>at <abbr title="Illuminate\Pipeline\Pipeline">Pipeline</abbr>->Illuminate\Pipeline\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Pipeline.php line 53">Pipeline.php line 53</a></li>
       <li>at <abbr title="Illuminate\Routing\Pipeline">Pipeline</abbr>->Illuminate\Routing\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/VerifyCsrfToken.php line 65">VerifyCsrfToken.php line 65</a></li>
       <li>at <abbr title="Illuminate\Foundation\Http\Middleware\VerifyCsrfToken">VerifyCsrfToken</abbr>->handle(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), <em>object</em>(<abbr title="Closure">Closure</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php line 148">Pipeline.php line 148</a></li>
       <li>at <abbr title="Illuminate\Pipeline\Pipeline">Pipeline</abbr>->Illuminate\Pipeline\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Pipeline.php line 53">Pipeline.php line 53</a></li>
       <li>at <abbr title="Illuminate\Routing\Pipeline">Pipeline</abbr>->Illuminate\Routing\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/View/Middleware/ShareErrorsFromSession.php line 49">ShareErrorsFromSession.php line 49</a></li>
       <li>at <abbr title="Illuminate\View\Middleware\ShareErrorsFromSession">ShareErrorsFromSession</abbr>->handle(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), <em>object</em>(<abbr title="Closure">Closure</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php line 148">Pipeline.php line 148</a></li>
       <li>at <abbr title="Illuminate\Pipeline\Pipeline">Pipeline</abbr>->Illuminate\Pipeline\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Pipeline.php line 53">Pipeline.php line 53</a></li>
       <li>at <abbr title="Illuminate\Routing\Pipeline">Pipeline</abbr>->Illuminate\Routing\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Session/Middleware/StartSession.php line 64">StartSession.php line 64</a></li>
       <li>at <abbr title="Illuminate\Session\Middleware\StartSession">StartSession</abbr>->handle(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), <em>object</em>(<abbr title="Closure">Closure</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php line 148">Pipeline.php line 148</a></li>
       <li>at <abbr title="Illuminate\Pipeline\Pipeline">Pipeline</abbr>->Illuminate\Pipeline\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Pipeline.php line 53">Pipeline.php line 53</a></li>
       <li>at <abbr title="Illuminate\Routing\Pipeline">Pipeline</abbr>->Illuminate\Routing\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Cookie/Middleware/AddQueuedCookiesToResponse.php line 37">AddQueuedCookiesToResponse.php line 37</a></li>
       <li>at <abbr title="Illuminate\Cookie\Middleware\AddQueuedCookiesToResponse">AddQueuedCookiesToResponse</abbr>->handle(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), <em>object</em>(<abbr title="Closure">Closure</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php line 148">Pipeline.php line 148</a></li>
       <li>at <abbr title="Illuminate\Pipeline\Pipeline">Pipeline</abbr>->Illuminate\Pipeline\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Pipeline.php line 53">Pipeline.php line 53</a></li>
       <li>at <abbr title="Illuminate\Routing\Pipeline">Pipeline</abbr>->Illuminate\Routing\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Cookie/Middleware/EncryptCookies.php line 59">EncryptCookies.php line 59</a></li>
       <li>at <abbr title="Illuminate\Cookie\Middleware\EncryptCookies">EncryptCookies</abbr>->handle(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), <em>object</em>(<abbr title="Closure">Closure</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php line 148">Pipeline.php line 148</a></li>
       <li>at <abbr title="Illuminate\Pipeline\Pipeline">Pipeline</abbr>->Illuminate\Pipeline\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Pipeline.php line 53">Pipeline.php line 53</a></li>
       <li>at <abbr title="Illuminate\Routing\Pipeline">Pipeline</abbr>->Illuminate\Routing\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php line 102">Pipeline.php line 102</a></li>
       <li>at <abbr title="Illuminate\Pipeline\Pipeline">Pipeline</abbr>->then(<em>object</em>(<abbr title="Closure">Closure</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Router.php line 561">Router.php line 561</a></li>
       <li>at <abbr title="Illuminate\Routing\Router">Router</abbr>->runRouteWithinStack(<em>object</em>(<abbr title="Illuminate\Routing\Route">Route</abbr>), <em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Router.php line 520">Router.php line 520</a></li>
       <li>at <abbr title="Illuminate\Routing\Router">Router</abbr>->dispatchToRoute(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Router.php line 498">Router.php line 498</a></li>
       <li>at <abbr title="Illuminate\Routing\Router">Router</abbr>->dispatch(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Foundation/Http/Kernel.php line 174">Kernel.php line 174</a></li>
       <li>at <abbr title="Illuminate\Foundation\Http\Kernel">Kernel</abbr>->Illuminate\Foundation\Http\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Pipeline.php line 30">Pipeline.php line 30</a></li>
       <li>at <abbr title="Illuminate\Routing\Pipeline">Pipeline</abbr>->Illuminate\Routing\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/TransformsRequest.php line 30">TransformsRequest.php line 30</a></li>
       <li>at <abbr title="Illuminate\Foundation\Http\Middleware\TransformsRequest">TransformsRequest</abbr>->handle(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), <em>object</em>(<abbr title="Closure">Closure</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php line 148">Pipeline.php line 148</a></li>
       <li>at <abbr title="Illuminate\Pipeline\Pipeline">Pipeline</abbr>->Illuminate\Pipeline\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Pipeline.php line 53">Pipeline.php line 53</a></li>
       <li>at <abbr title="Illuminate\Routing\Pipeline">Pipeline</abbr>->Illuminate\Routing\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/TransformsRequest.php line 30">TransformsRequest.php line 30</a></li>
       <li>at <abbr title="Illuminate\Foundation\Http\Middleware\TransformsRequest">TransformsRequest</abbr>->handle(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), <em>object</em>(<abbr title="Closure">Closure</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php line 148">Pipeline.php line 148</a></li>
       <li>at <abbr title="Illuminate\Pipeline\Pipeline">Pipeline</abbr>->Illuminate\Pipeline\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Pipeline.php line 53">Pipeline.php line 53</a></li>
       <li>at <abbr title="Illuminate\Routing\Pipeline">Pipeline</abbr>->Illuminate\Routing\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/ValidatePostSize.php line 27">ValidatePostSize.php line 27</a></li>
       <li>at <abbr title="Illuminate\Foundation\Http\Middleware\ValidatePostSize">ValidatePostSize</abbr>->handle(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), <em>object</em>(<abbr title="Closure">Closure</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php line 148">Pipeline.php line 148</a></li>
       <li>at <abbr title="Illuminate\Pipeline\Pipeline">Pipeline</abbr>->Illuminate\Pipeline\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Pipeline.php line 53">Pipeline.php line 53</a></li>
       <li>at <abbr title="Illuminate\Routing\Pipeline">Pipeline</abbr>->Illuminate\Routing\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Foundation/Http/Middleware/CheckForMaintenanceMode.php line 46">CheckForMaintenanceMode.php line 46</a></li>
       <li>at <abbr title="Illuminate\Foundation\Http\Middleware\CheckForMaintenanceMode">CheckForMaintenanceMode</abbr>->handle(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>), <em>object</em>(<abbr title="Closure">Closure</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php line 148">Pipeline.php line 148</a></li>
       <li>at <abbr title="Illuminate\Pipeline\Pipeline">Pipeline</abbr>->Illuminate\Pipeline\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Routing/Pipeline.php line 53">Pipeline.php line 53</a></li>
       <li>at <abbr title="Illuminate\Routing\Pipeline">Pipeline</abbr>->Illuminate\Routing\{closure}(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Pipeline/Pipeline.php line 102">Pipeline.php line 102</a></li>
       <li>at <abbr title="Illuminate\Pipeline\Pipeline">Pipeline</abbr>->then(<em>object</em>(<abbr title="Closure">Closure</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Foundation/Http/Kernel.php line 149">Kernel.php line 149</a></li>
       <li>at <abbr title="Illuminate\Foundation\Http\Kernel">Kernel</abbr>->sendRequestThroughRouter(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/vendor/laravel/framework/src/Illuminate/Foundation/Http/Kernel.php line 116">Kernel.php line 116</a></li>
       <li>at <abbr title="Illuminate\Foundation\Http\Kernel">Kernel</abbr>->handle(<em>object</em>(<abbr title="Illuminate\Http\Request">Request</abbr>)) in <a title="/home/pi/test/public/index.php line 53">index.php line 53</a></li>
       <li>at <abbr title=""></abbr>require_once('/home/pi/test/public/index.php') in <a title="/home/pi/test/server.php line 21">server.php line 21</a></li>
    </ol>
</div>

            </div>
    </body>
</html>
