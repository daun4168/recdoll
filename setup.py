from distutils.core import setup

setup(
    name='Recdoll',
    packages=['Recdoll'],
    version='0.0..1',
    license='MIT',
    description='Best Recommendation Library',   # Give a short description about your library
    author='Daun Jeong',
    author_email='daun.jeong@navercorp.com',
    url='https://github.com/daun4168/recdoll',
    download_url='https://github.com/daun4168/recdoll/archive/v_01.tar.gz',    # I explain this later on
    keywords=['Recommendation', 'Machine Learning'],   # Keywords that define your package best
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)