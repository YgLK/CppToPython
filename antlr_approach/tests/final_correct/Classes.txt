using namespace std;

class Car{
    int year = 2019;
    private:
        int speed = 120;
    private:
        int gear = 3;
    public:
        string name = "Carl";
    protected:
        bool isSafe = true;
};

class Giraffe{
    private:
        int length = 3;
    public:
        int height = 13;

    public:
        int getHeight(){
            return height;
        }
    protected:
        int getHeight(){
            return height;
        }
    private:
        int getLength(){
            return length;
        }
};

int main(){
cout << "Classes";
};
