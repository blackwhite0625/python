bob = {
    "po1":"sos",
    "po2":"coco",
    "po3":"momo",
    "po4":"roro"
}

#get
print(bob.get("po1"))
print(bob.get("po3"))

#update 新增
bob.update({"po5":"popo"})
print(bob)

#pop 刪除
bob.pop("po2")
print(bob)

#values 所有值
print(bob.values())

#items
print(bob.items())
