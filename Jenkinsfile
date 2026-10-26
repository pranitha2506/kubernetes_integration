pipeline{
    agent any
    stages{
        stage('build'){
            steps{
                echo 'build docker image'
                bat 'build -t mypythonflaskapp'
            }
        }
        stage('run'){
            steps{
                echo 'run the docker container'
                bat 'build -r -p container ||exit 0'
            }
        }
        stage('Docker login'){
            steps{
                
                bat 'docker login: -u padthampranitha -p Pranitha@123' 
            }
        }
    }
    post{
        success{
            echo the application run successfully
        }
        failure{
            echo the application failed check logs.
        }
    }
}