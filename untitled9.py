# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SmTd8Hqgm7FkSjcmT5x94NM47Vfu_OaS
"""

def kasallik_tashxisi(belgi):
  if belgi == "istima":
    return "Parastemol iching "
  elif belgi=="bosh ogrigi":
    return "bolnol"
  elif belgi=="tish ogrigi":
    return "sinipar"
  if belgi=="tizza ogrigi":
    return "kupen"
  elif belgi=="suyaklar ogrigi":
    return "kalsiy "
  elif belgi=="bel ogrisa":
    return "Voltaren gel"
  elif belgi=="koz ogrigi":
    return "Refresh Tears"
  elif belgi=="qorin ogrigi":
    return "Mezim"
  elif belgi=="Burun bitishi":
    return "Xylometazoline"
  elif belgi=="Og'iz va tomoq":
    return "Septolete"
  elif belgi=="Qon bosimini tushirish":
    return "Enalapri"
  elif belgi=="Mushak va bo‘g‘imlar":
    return "Fastum gel"
  elif belgi=="Infeksiya":
    return "Tobrex (tobramitsin)"
  else:
    return "shifokorga murojat qilin"
  belgi =input ("kasallik belgisini kiritin")
  natija=kasallik_tashxisi(belgi)
  print(natija)