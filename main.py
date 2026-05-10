Masalaning sharti: Funksiyalar.

```python
def salom(ism):
    """Salom so'zini chiqaruvchi funksiya"""
    return f"Salom, {ism}!"

def yoshni_top(sana):
    """Yoshni topuvchi funksiya"""
    import datetime
    tugilgan_sana = datetime.datetime.strptime(sana, "%Y-%m-%d")
    yosh = datetime.datetime.now().year - tugilgan_sana.year
    return yosh

def katta_kichik_sonlar(sonlar):
    """Katta va kichik sonlarni topuvchi funksiya"""
    katta_son = max(sonlar)
    kichik_son = min(sonlar)
    return katta_son, kichik_son

def fibonacci(n):
    """Fibonacci sonlarini topuvchi funksiya"""
    if n <= 0:
        return "Fibonacci sonlari 0 dan boshlanadi"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def sonni_qayta_yozish(son):
    """Sonni qayta yozuvchi funksiya"""
    return str(son)

def sonni_katta_qilish(son):
    """Sonni katta qiluvchi funksiya"""
    return son + 1

def sonni_kichik_qilish(son):
    """Sonni kichik qiluvchi funksiya"""
    return son - 1
```

Bu funksiyalar quyidagi vazifalarni bajaradi:

1. `salom` funksiyasi salom so'zini chiqaradi.
2. `yoshni_top` funksiyasi yoshni topadi.
3. `katta_kichik_sonlar` funksiyasi katta va kichik sonlarni topadi.
4. `fibonacci` funksiyasi Fibonacci sonlarini topadi.
5. `sonni_qayta_yozish` funksiyasi sonni qayta yozadi.
6. `sonni_katta_qilish` funksiyasi sonni katta qiladi.
7. `sonni_kichik_qilish` funksiyasi sonni kichik qiladi.
