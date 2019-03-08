$(function() {
    //定义变量，决定最终是否可以提交表单
    var error_name = false;//默认没有错误
    var error_pwd = false;
    var error_cpwd = false;
    var error_email = false;

    //失去焦点时验证用户名
    $('#username').blur(function () {
        check_username();
    });
    //获取焦点时隐藏提示信息
    $('#username').focus(function () {
        $(this).error_tip.hide();
    });

    function check_username() {
        var val = $('#username').val();
        var re = /^\w{5,15}$/i;//匹配字母数字下划线，5到15位，忽略大小写

        if (val == '') {
            $('.error_tip').html('用户名不能为空！');
            $('.error_tip').show();
            error_name = true;
            return;
        }

        if (re.test(val)) {
            error_name = false;
        } else {
            $('.error_tip').html('用户名是包含数字、字母、下划线的5-15位字符');
            $('.error_tip').show();
            error_name = true;
            return;
        }
    }

    $('#passwd1').blur(function() {
        check_pwd();
	});
	$('#passwd1').focus(function() {
		$(this).error_tip.hide();
	});

		function check_pwd(){
		var val = $('#passwd1').val();
		var re = /^[a-zA-Z0-9@\$\*\.\!\?]{6,16}$/;//[]表示范围，允许字母数字@$*.!?，6-16位

		if(val == ''){
			$('.error_tip').html('密码不能为空！');
			$('.error_tip').show();
			error_pwd = true;
			return;
		}

		if(re.test(val)){
			error_pwd = false;
		}else{
			$('.error_tip').html('密码是包含数字、字母、@$*.!?的6-16位字符');
			$('.error_tip').show();
			error_pwd = true;
			return;
		}
	}

	$('#password2').blur(function() {
        check_cpwd();
	});
	$('#password2').focus(function() {
		$(this).error_tip.hide();
	});

	function check_cpwd(){
		var val = $('#password1').val();
		var cval = $('#password2').val();

		if(val == cval){
			error_cpwd = false;
		}else{
			$('.error_tip').html('再次输入的密码不一致！');
			$('.error_tip').show();
			error_cpwd = true;
			return;
		}
	}


	$('#email').blur(function() {
		check_email();
	});
	$('#email').focus(function() {
		$(this).error_tip.hide();
	});


    function check_email(){
		var val = $('#email').val();
		var re =  /^\w{4}$/i;

		if(val == ''){
			$('.error_tip').html('验证码不能为空！');
			$('.error_tip').show();
			error_email = true;
			return;
		}

		if(re.test(val)){
			error_email = false;
		}else{
			$('.error_tip').html('验证码格式不正确');
			$('.error_tip').show();
			error_email = true;
			return;
		}
	}

    $('.form').submit(function() {
        //防止用户上来就直接点提交，上面验证都未执行，所以先执行一次
        check_username();
		check_pwd();
		check_email();

		if(!(error_name == false && error_pwd == false && error_email == false && error_cpwd == false)){
			return false;
		}
	});
})
