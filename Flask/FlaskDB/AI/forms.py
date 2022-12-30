from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField , PasswordField , EmailField
from wtforms.validators import DataRequired , Length , EqualTo , Email

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=20)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 다릅니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    name = StringField('이름' , validators=[DataRequired() , Length(min=3 , max=20)])
    birthday = StringField('생년월일' , validators=[DataRequired() , Length(min=8 , max=8)])
    gender = StringField("성별" , validators=[DataRequired() , Length(min=1 , max=8)])
    address1 = StringField('주소' , validators=[DataRequired()])
    address2 = StringField('상세주소' , validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    phone = StringField('전화번호', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름' , validators=[DataRequired('ID를 확인해주세요'), Length(min=3 , max=25)])
    password = PasswordField('비밀번호' , validators=[DataRequired('비밀번호를 확인해주세요')])

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])        # 한줄만 넣을 수 있음
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])     # 여러줄을 넣을 수 있음

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])