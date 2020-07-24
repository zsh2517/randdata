from generators import gen
from DataSet import DataSet
from OutputMgr import OutputMgr

ds: DataSet = DataSet()
mgr: OutputMgr = OutputMgr()
g_email: gen.email = gen.email()
g_str: gen.string = gen.string()
g_tel: gen.tel = gen.tel()
ds.set("用户名", g_email, {})
ds.set("密码", g_str, {})
ds.set("手机号", g_tel, {})
ds.gen_multi(15)
ds.output(mgr)
