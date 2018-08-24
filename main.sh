#! bin/bash

while ! [ $? -gt 0 ]; do
    case "$1" in
                -h|--help)
                        echo "$package - attempt to capture frames"
                        echo " "
                        echo "$package [options] application [arguments]"
                        echo " "
                        echo "options:"
                        echo "-h, --help                show brief help"
                        echo "-f, --file=FILE           specify an file to use"
                        echo "-to, --timeout=TIMEOUT    specify a timeout od while loop"
                        exit 0
                        ;;
                -f)
                        shift
                        if test $# -gt 0; then
                                export FILE=$1
                        else
                                echo "no file specified"
                                exit 1
                        fi
                        shift
                        ;;
                --file*)
                        export FILE=`echo $1 | sed -e 's/^[^=]*=//g'`
                        shift
                        ;;
                -to)
                        shift
                        if test $# -gt 0; then
                                export TIMEOUT=$1
                        else
                                echo "no timeout specified"
                                exit 1
                        fi
                        shift
                        ;;
                --timeout*)
                        export TIMEOUT=`echo $1 | sed -e 's/^[^=]*=//g'`
                        shift
                        ;;
                *)
                        break
                        ;;
        esac
done

if [ ${FILE} != FILE ] && [ ${TIMEOUT} != TIMEOUT ]; then
    printf "SERVER MONITOR STARTED \n"
    printf "nohup lof file created in project folder \n"
    while true; do
        nohup python3 main.py --confile ${FILE} &
        sleep ${TIMEOUT}
    done;
else
    echo "Arguments missing"
fi

