FROM public.ecr.aws/lambda/python:3.8 as base

COPY ./src ${LAMBDA_TASK_ROOT}
COPY ./config /var/config
RUN yum -y update  \
    && yum -y install which gcc \
    && pip3 install pipenv
CMD [ "handler.lambda_handler" ]

FROM base as prodGrade

RUN cd /var/config  \
    && pipenv install --system --ignore-pipfile  \
    && rm -R /var/config \
    && ZAPPA_HANDLER_PATH=$(python -c "from zappa import handler; print (handler.__file__)") \
    && cp $ZAPPA_HANDLER_PATH ${LAMBDA_TASK_ROOT}

FROM base as devGrade

RUN echo $TERM > /term.tct
RUN which python > /python.txt
RUN cd /var/config \
    && pipenv install --dev --system --ignore-pipfile  \
    && rm -R /var/config \
    && ZAPPA_HANDLER_PATH=$(python -c "from zappa import handler; print (handler.__file__)") \
    && cp $ZAPPA_HANDLER_PATH ${LAMBDA_TASK_ROOT}
