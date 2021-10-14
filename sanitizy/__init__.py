import html,pymysql,sys
from werkzeug.utils import secure_filename

class XSS:

    def __init__(self,obj):
        self.request=obj

    def escape(self,s):
        return html.escape(s,quote=True)

    def escape_form(self):
        d={}
        for x in dict(self.request.form):
            d.update({x:self.escape(dict(self.request.form)[x][0])}) if  sys.version_info < (3,0) else d.update({x:self.escape(dict(self.request.form)[x])})
        return d

    def escape_args(self):
        d={}
        for x in dict(self.request.args):
            d.update({x:self.escape(dict(self.request.form)[x][0])}) if  sys.version_info < (3,0) else d.update({x:self.escape(dict(self.request.form)[x])})
        return d


class CSRF:

    def __init__(self,obj,allowed_domains=[]):
        self.request=obj
        self.allowed_domains=allowed_domains if (allowed_domains and len(allowed_domains)>0) else [self.request.host]

    def validate(self):
        referer=self.request.headers.get('Referer','')
        if referer.strip()=="" or referer.strip().lower()=="null":
            return False
        a=referer.split("://")[1].split("/")[0]
        if a in self.allowed_domains:
            return True
        return False


class SQL:

    def __init__(self,obj):
        self.request=obj

    def escape(self,s):
        return pymysql.converters.escape_string(s)

    def escape_form(self):
        d={}
        for x in dict(self.request.form):
            d.update({x:self.escape(dict(self.request.form)[x][0])}) if  sys.version_info < (3,0) else d.update({x:self.escape(dict(self.request.form)[x])})
        return d

    def escape_args(self):
        d={}
        for x in dict(self.request.args):
            d.update({x:self.escape(dict(self.request.form)[x][0])}) if  sys.version_info < (3,0) else d.update({x:self.escape(dict(self.request.form)[x])})
        return d


class file_upload:

    def __init__(self,allowed_extensions=['png','jpg','jpeg','gif','pdf'],allowed_mimetypes=["application/pdf","application/x-pdf","image/png","image/jpg","image/jpeg"]):
        self.allowed_extensions=allowed_extensions
        self.allowed_mimetypes=allowed_mimetypes

    def check_file(self,f):
        return self.valid_file(f,self.allowed_extensions,self.allowed_mimetypes)

    def valid_extension(self,f,extentions):
        try:
            return f.split(".")[1].lower() in extentions
        except:
            return False

    def valid_mimetype(self,f,mimetypes):
        try:
            return f.content_type.lower() in mimetypes
        except:
            return False

    def valid_file(self,f,extentions,mimetypes):
        return self.valid_extension(self.secure_filename(f),extentions) and self.valid_mimetype(f,mimetypes)

    def secure_filename(self,f):
        return secure_filename(".".join(f.filename.split(".")[:2]))

    def save_file(self,f):
        f.save(self.secure_filename(f))
