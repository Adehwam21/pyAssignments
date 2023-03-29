<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php

    class StudentRegistration
    {
        
        private $studentName;
        private $registrationDate;

        public function setStudentName($studentName)
        {
            $this->studentName = $studentName;
        }

        public function getStudentName()
        {
            return $this->studentName;
        }

        public function setRegistrationDate($registrationDate)
        {
            $this->registrationDate = $registrationDate;
        }

        public function getRegistrationDate()
        {
            return $this->registrationDate;
        }

        public function daysSinceRegistration()
        {
            $today = new DateTime();
            $diff = $today->diff($this->registrationDate);
            return $diff->days;
        }

    }

    $student = new StudentRegistration();
    $student->setStudentName('John Doe');
    $student->setRegistrationDate(new DateTime('2018-01-01'));
    echo $student->getStudentName() . ' registered on ' . $student->getRegistrationDate()->format('Y-m-d') . ' which was ' . $student->daysSinceRegistration() . ' days ago';

    ?>
</body>

</html>