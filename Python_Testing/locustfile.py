
from locust import task, run_single_user
from locust import FastHttpUser


class myrec_get(FastHttpUser):
    host = "http://localhost:5000"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Cookie": "csrftoken=bI3LY2E5CbQFE2h7HZ1HC6Sb8tKXZNVo; sessionid=8fxmq6w2kdfguwr29ix2k9ihqruq43cb",
        "Host": "localhost:5000",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/styles.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "If-Modified-Since": "Wed, 06 Mar 2024 10:42:44 GMT",
                "If-None-Match": '"1709721764.881601-277-3918668356"',
                "Referer": "http://localhost:5000/",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,*/*",
                "Referer": "http://localhost:5000/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-origin",
            },
            catch_response=True,
        ) as resp:
            pass


class myrec_purchasePlaces(FastHttpUser):
    host = "http://localhost:5000"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Cookie": "csrftoken=bI3LY2E5CbQFE2h7HZ1HC6Sb8tKXZNVo; sessionid=8fxmq6w2kdfguwr29ix2k9ihqruq43cb",
        "Host": "localhost:5000",
        "Referer": "http://localhost:5000/purchasePlaces",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    }

    @task
    def t(self):
        with self.client.request(
            "POST",
            "/purchasePlaces",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Content-Length": "48",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "http://localhost:5000",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            data="club=Simply+Lift&competition=New+Winter&places=1",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,*/*",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
            },
            catch_response=True,
        ) as resp:
            pass


class myrec_showSummary(FastHttpUser):
    host = "http://localhost:5000"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Cookie": "csrftoken=bI3LY2E5CbQFE2h7HZ1HC6Sb8tKXZNVo; sessionid=8fxmq6w2kdfguwr29ix2k9ihqruq43cb",
        "Host": "localhost:5000",
        "Referer": "http://localhost:5000/showSummary",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    }

    @task
    def t(self):
        with self.client.request(
            "POST",
            "/showSummary",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Content-Length": "26",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "http://localhost:5000",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            data="email=john%40simplylift.co",
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,*/*",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
            },
            catch_response=True,
        ) as resp:
            pass


class myrec_logout(FastHttpUser):
    host = "http://localhost:5000"
    default_headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Cookie": "csrftoken=bI3LY2E5CbQFE2h7HZ1HC6Sb8tKXZNVo; sessionid=8fxmq6w2kdfguwr29ix2k9ihqruq43cb",
        "Host": "localhost:5000",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/logout",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Referer": "http://localhost:5000/purchasePlaces",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/",
            headers={
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Referer": "http://localhost:5000/purchasePlaces",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/styles.css",
            headers={
                "Accept": "text/css,*/*;q=0.1",
                "Referer": "http://localhost:5000/",
                "Sec-Fetch-Dest": "style",
                "Sec-Fetch-Mode": "no-cors",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/favicon.ico",
            headers={
                "Accept": "image/avif,image/webp,*/*",
                "Referer": "http://localhost:5000/",
                "Sec-Fetch-Dest": "image",
                "Sec-Fetch-Mode": "no-cors",
            },
            catch_response=True,
        ) as resp:
            pass

