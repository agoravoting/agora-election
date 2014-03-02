/*
    This file is part of agora-election.
    Copyright (C) 2014 Eduardo Robles Elvira <edulix AT agoravoting DOT com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

(function(){

    var AE = this.AE = {}; // AE  means "Agora Election"
    var app = this.app = {};
    app.current_view = null;

    var Checker = {};
    Checker.email = function(v) {
        var RFC822;
        RFC822 = /^([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22))*\x40([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d))*$/;
        return RFC822.test(v);
    };

    Checker.tlf = function (tlf) {
        if (!tlf) {
            return null;
        }
        tlf = tlf.trim();
        tlf = tlf.replace(/ /g, '');
        tlf = tlf.replace(/^0034/, "+34");
        if (!/^\+34/.test(tlf)) {
            tlf = "+34" + tlf;
        }
        var regExp = new RegExp(app_data.tlf_no_rx);
        if (!regExp.test(tlf)) {
            return null;
        }
        return tlf;
    };

    /**
     *  Main function, creates the router and starts the routing processing
     */
    var main = function() {
        // Initiate the router
        app.router = new AE.Router();

        // Start Backbone history a necessary step for bookmarkable URL's
        Backbone.history.start();
    };

    /**
     * Url router, launches the appropiate views depending on the current
     * #hashbang
     */
    AE.Router = Backbone.Router.extend({
        routes: {
            "": "home",
            "identify": "identify",
            "verify-sms": "verify_sms"
        },

        home: function() {
            console.log("home!");
            app.current_view = new AE.HomeView();
        },

        identify: function() {
            app.current_view = new AE.IdentifyView();
        },

        verify_sms: function() {
            app.current_view = new AE.VerifySMSView();
        }
    });

    /**
     * Home view - just renders the home page template with the app_data
     */
    AE.HomeView = Backbone.View.extend({
        el: "#renderall",

        initialize: function() {
            this.template = _.template($("#template-home-view").html());
            this.render();
        },

        render: function() {
            this.$el.html(this.template(app_data));
            this.delegateEvents();
            return this;
        }
    });

    /**
     * Identify view - shows the form where the user enters identification
     * details, most importantly the telephone number.
     */
    AE.IdentifyView = Backbone.View.extend({
        el: "#renderall",

        events: {
            'click #identify-action': 'processForm'
        },

        initialize: function() {
            this.template = _.template($("#template-identify-view").html());
            this.render();
        },

        render: function() {
            this.$el.html(this.template(app_data));
            this.delegateEvents();
            return this;
        },

        /**
         * Used in setError and processForm to detect errors
         */
        errorFlag: false,

        /**
         * detects when we are sending a petition
         */
        sendingFlag: false,

        /**
         *  Help function to set the
         */
        setError: function(selector, text) {
            this.errorFlag = true;
            $(selector).parent().find(".help-block").html(text);
            $(selector).closest(".form-group").addClass("has-error");
        },

        /**
         * Does the heavy duty stuff in this view, processes the form, showing
         * errors if any, or sending the data and showing the SMS code
         * verification form.
         */
        processForm: function(e) {
            if (this.sendingFlag) {
                return;
            }
            // reset errors
            this.errorFlag = false;
            $("#identify-action").attr("disabled", "disabled");
            $(".form-group.has-error .help-block").each(function() {
                $(this).html("");
            });
            $(".form-group").removeClass("has-error");

            // get the data
            var first_name = $("#first-name").val().trim();
            var last_name = $("#last-name").val().trim();
            var email = $("#email").val().trim();
            var tlf = $("#tlf").val().trim();
            var postal_code = parseInt($("#postal-code").val().trim());
            var above_age = $("#above-age:checked").length == 1;
            var mail_updates = $("#receive-mail-updates:checked").length == 1;
            var accept_conditions = $("#accept-conditions:checked").length == 1;

            // start checking
            if (first_name.length < 3 || first_name.length >= 60)
            {
                this.setError("#first-name", "Obligatorio, de 3 a 60 caracteres");
            }

            if (last_name.length < 3 || last_name.length >= 100)
            {
                this.setError("#last-name", "Obligatorio, de 3 a 60 caracteres");
            }

            if (email.length < 3 || email.length >= 140 ||
                    !Checker.email(email))
            {
                this.setError("#email", "Debes introducir una dirección email válida");
            }

            app_data.tlf = Checker.tlf(tlf)
            if (!app_data.tlf) {
                this.setError("#tlf", "Debes introducir un teléfono español válido. Ejemplo: 666 666 666");
            }

            if (!/^[0-9]+$/.test(postal_code) || postal_code < 1 || postal_code > 100000)
            {
                this.setError("#postal-code", "Código postal inválido");
            }

            if (!above_age) {
                this.setError("#above-age", "Debes ser mayor de edad para votar");
            }

            if (!accept_conditions) {
                this.setError("#accept-conditions", "Debes aceptar las condiciones para votar");
            }

            if (this.errorFlag) {
                $("#identify-action").removeAttr("disabled");
                return;
            }

            this.sendingFlag = true;

            var inputData = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "tlf": app_data.tlf,
                "postal_code": postal_code,
                "receive_updates": mail_updates
            };

            var self = this;
            var jqxhr = $.ajax("/api/v1/register/", {
                data: JSON.stringify(inputData),
                contentType : 'application/json',
                type: 'POST',
            })
            .done(function(data) {
                console.log("data = ");
                console.log(data);
                self.sendingFlag = false;
                app.router.navigate("verify-sms", {trigger: true});
            })
            .fail(this.processError);
        },

        showErrorMessage: function(message, allow_try_again) {
            $("#error-message").html(message);
            if (allow_try_again) {
                $("#identify-action").removeAttr("disabled");
            }
        },

        processError: function(jqXHR, textStatus) {
            var self = app.current_view;
            self.sendingFlag = false;
            console.log("fail = " + jqXHR.responseText);
            try {
                var data = JSON.parse(jqXHR.responseText);
            } catch(e) {
                self.showErrorMessage('Ha ocurrido un error interno enviando el ' +
                'formulario. Por favor, ponte en <a href="#contact">contacto ' +
                'con nosotros</a> explicando en detalle los pasos que seguiste ' +
                'para que podamos reproducir y arreglar el problema.', false);
                return;
            }
            if (data.error_codename == "already_voted") {
                self.showErrorMessage('¡Vaya! Ya votaste anteriormente, no ' +
                'puedes votar dos veces.', false);
            } else if (data.error_codename == "blacklisted") {
                self.showErrorMessage('¡Vaya! Tu petición ha sido bloqueada. Puede ' +
                'que sea un error, o que alguien haya estado haciendo ' +
                'cosas raras. Si quieres puedes <a href="#contact">contactar ' +
                'con nosotros</a> para contarnos tu problema.', false);
            } else if (data.error_codename == "wait_hour") {
                self.showErrorMessage('¡Vaya! Has hecho demasiadas peticiones ' +
                'seguidas. Por seguridad, tendrás que esperar una hora para ' +
                'intentarlo de nuevo. Si quieres puedes ' +
                '<a href="#contact">contactar con nosotros</a> para contarnos ' +
                'tu problema.', false);
            } else if (data.error_codename == "wait_day") {
                self.showErrorMessage('¡Vaya! Has hecho demasiadas peticiones ' +
                'seguidas hoy. Por seguridad, se han bloqueado tus peticiones ' +
                'durante 24 horas. Si quieres puedes <a href="#contact">' +
                'contactar con nosotros</a> para contarnos tu problema.', false);
            } else if (data.error_codename == "wait_expire") {
                self.showErrorMessage('¡Ten paciencia! Te acabamos de enviar un SMS' +
                ' hace nada, espera a que te llegue y cuando te llegue ' +
                '<a href="#verify-sms">pincha aquí para ' +
                'verificar tu código SMS</a>.', false);
            } else {
                self.showErrorMessage('Ha ocurrido un error interno enviando el ' +
                'formulario. Por favor, ponte en <a href="#contact">contacto ' +
                'con nosotros</a> explicando en detalle los pasos que seguiste ' +
                'para que podamos reproducir y arreglar el problema.', false);
            }
        }
    });

    /**
     * Verify SMS view
     */
    AE.VerifySMSView = Backbone.View.extend({
        el: "#renderall",

        events: {
            'click #verify-action': 'processForm'
        },

        initialize: function() {
            this.template = _.template($("#template-verify-sms-view").html());
            this.render();
        },

        render: function() {
            if (!app_data.tlf) {
                app_data.tlf = null;
            }
            this.$el.html(this.template(app_data));
            this.delegateEvents();
            return this;
        },

        /**
         * Used in setError and processForm to detect errors
         */
        errorFlag: false,

        /**
         * detects when we are sending a petition
         */
        sendingFlag: false,

        /**
         *  Help function to set the
         */
        setError: function(selector, text) {
            this.errorFlag = true;
            $(selector).parent().find(".help-block").html(text);
            $(selector).closest(".form-group").addClass("has-error");
        },

        /**
         * Does the heavy duty stuff in this view, processes the form, showing
         * errors if any, or sending the data and showing the SMS code
         * verification form.
         */
        processForm: function(e) {
            if (this.sendingFlag) {
                return;
            }
            // reset errors
            this.errorFlag = false;
            $("#verify-action").attr("disabled", "disabled");
            $(".form-group.has-error .help-block").each(function() {
                $(this).html("");
            });
            $(".form-group").removeClass("has-error");

            // get the data
            var tlf = null;
            if (app_data.tlf) {
                tlf = app_data.tlf;
            } else {
                tlf = $("#tlf").val();
            }
            var sms_code = $("#sms-code").val().trim().toUpperCase();

            // start checking
            if (sms_code.length != 8)
            {
                this.setError("#sms-code", "Código introducido inválido");
            }

            tlf = Checker.tlf(tlf)
            if (!tlf) {
                this.setError("#tlf", "Debes introducir un teléfono español válido. Ejemplo: 666 666 666");
            }

            var inputData = {
                "tlf": tlf,
                "token": sms_code
            };

            var self = this;
            var jqxhr = $.ajax("/api/v1/sms_auth/", {
                data: JSON.stringify(inputData),
                contentType : 'application/json',
                type: 'POST',
            })
            .done(function(data) {
                console.log("data = ");
                try {
                    data = JSON.parse(data);
                } catch(e) {
                    self.showErrorMessage('Ha ocurrido un error interno enviando el ' +
                    'formulario. Por favor, ponte en <a href="#contact">contacto ' +
                    'con nosotros</a> explicando en detalle los pasos que seguiste ' +
                    'para que podamos reproducir y arreglar el problema.', false);
                    return;
                }
                var url = app_data.election_url + "?message=" + encodeURIComponent(data.message) + "&sha1_hmac=" + encodeURIComponent(data.sha1_hmac);
                document.location.href=url;
            })
            .fail(this.processError);
        },

        showErrorMessage: function(message, allow_try_again) {
            $("#error-message").html(message);
            if (allow_try_again) {
                $("#identify-action").removeAttr("disabled");
            }
        },

        processError: function(jqXHR, textStatus) {
            var self = app.current_view;
            self.sendingFlag = false;
            console.log("fail = " + jqXHR.responseText);
            try {
                var data = JSON.parse(jqXHR.responseText);
            } catch(e) {
                self.showErrorMessage('Ha ocurrido un error interno enviando el ' +
                'formulario. Por favor, ponte en <a href="#contact">contacto ' +
                'con nosotros</a> explicando en detalle los pasos que seguiste ' +
                'para que podamos reproducir y arreglar el problema.', false);
                return;
            }
            if (data.error_codename == "already_voted") {
                self.showErrorMessage('¡Vaya! Ya votaste anteriormente, no ' +
                'puedes votar dos veces.', false);
            } else if (data.error_codename == "sms_notsent") {
                self.showErrorMessage('No tienes ningún mensaje SMS pendiente de verificar, debes ' +
                '<a href="#identify">identificarte</a> primero/de nuevo.', false);
            } else if (data.error_codename == "need_new_token") {
                self.showErrorMessage('¡Vaya! Se te han acabado el número ' +
                'de intentos para escribir el código SMS. Deberás ' +
                '<a href="#identify">identificarte</a> de nuevo.', false);
            } else if (data.error_codename == "invalid_token") {
                self.showErrorMessage('¡Vaya! El código SMS que has ' +
                    'introducido es incorrecto, por favor compruébalo.', true);
            } else {
                self.showErrorMessage('Ha ocurrido un error interno enviando el ' +
                'formulario. Por favor, ponte en <a href="#contact">contacto ' +
                'con nosotros</a> explicando en detalle los pasos que seguiste ' +
                'para que podamos reproducir y arreglar el problema.', false);
            }
        }
    });

    main();
}).call(this);
