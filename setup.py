from distutils.core import setup
VERSION = '0.4.0'
setup(name='httplib2',
        version=VERSION, 
        author='Joe Gregorio',
        author_email='joe@bitworking.org',
        url='http://bitworking.org/projects/httplib2/',
        download_url='http://bitworking.org/projects/httplib2/dist/httplib2-%s.tar.gz' % VERSION,
        description='A comprehensive HTTP client library.',
        license='MIT',
        long_description="""

A comprehensive HTTP client library, ``httplib2`` supports many features left out of other HTTP libraries.

**HTTP and HTTPS**
  HTTPS support is only available if the socket module was compiled with SSL support. 
 

**Keep-Alive**
  Supports HTTP 1.1 Keep-Alive, keeping the socket open and performing multiple requests over the same connection if possible. 


**Authentication**
  The following three types of HTTP Authentication are supported. These can be used over both HTTP and HTTPS.

  * Digest
  * Basic
  * WSSE

**Caching**
  The module can optionally operate with a private cache that understands the Cache-Control: 
  header and uses both the ETag and Last-Modified cache validators. Both file system
  and memcached based caches are supported.


**All Methods**
  The module can handle any HTTP request method, not just GET and POST.


**Redirects**
  Automatically follows 3XX redirects on GETs.


**Compression**
  Handles both 'deflate' and 'gzip' types of compression.


**Lost update support**
  Automatically adds back ETags into PUT requests to resources we have already cached. This implements Section 3.2 of Detecting the Lost Update Problem Using Unreserved Checkout


**Unit Tested**
  A large and growing set of unit tests.
        """,
        packages=['httplib2'],
        classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        ],
        )

