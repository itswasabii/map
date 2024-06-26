import React from "react";
import { Box, Container, Heading, Text, Button,Image, Flex } from "@chakra-ui/react";
import hero_img from "../assets/moringa.jpeg";
import { Grid, GridItem } from "@chakra-ui/react";
import History from "../components/History";
import Testimonials from "../components/Testimonials";

const SuccessStories = () => {
  return (
    <Box letterSpacing={"1px"} mt={"60px"}>
      {/* hero section */}
      <Box bg={"#101F3C"} color={"#fff"}>
        <Flex
          px={{ base: 5, md: 50 }}
          pt={"50px"}
          align={"strech"}
          // justify={"center"}
          flexDir={{ base: "column", lg: "row" }}
          gap={"2"}
          py={{ base: 2, md: 4, lg: 8 }}
        >
          <Box width={{ base: "100%", lg: "50%" }}>
            <Heading
              as="h1"
              fontSize={{ base: "2rem", md: "3rem" }}
              py={{ base: 2, md: 4, lg: 8 }}
            >
              Success Stories
            </Heading>
            <Text w={"auto"} pb={4}>
              Moringa fosters student and alumni engagement with a job success
              acquisition rate of 95%. This remarkable figure underscores
              Moringa's commitment to empowering its community members in their
              professional journeys.
              <Text as={"span"} display={{ base: "none", md: "inline" }}>
                {" "}
                By providing comprehensive support and resources, Moringa
                ensures that students and alumni are equipped with the skills
                and opportunities needed to succeed in their careers.
              </Text>
            </Text>
            <Flex flexWrap={"wrap"} gap={"20px"}>
              <Box w={{ base: 150, md: 200, lg: 250 }}>
                <Text fontWeight="bold" fontSize={{ base: "2rem", md: "3rem" }}>
                  #1
                </Text>
                <Text fontSize={{ base: "sm", md: "md" }}>
                  Benefit for alumni is career assistance
                </Text>
              </Box>
              <Box w={{ base: 150, md: 200, lg: 250 }}>
                <Text fontWeight="bold" fontSize={{ base: "2rem", md: "3rem" }}>
                  3,000
                </Text>
                <Text fontSize={{ base: "sm", md: "md" }}>
                  Alumnus joined Moringa at launch
                </Text>
              </Box>
              <Box w={{ base: 150, md: 200, lg: 250 }}>
                <Text fontWeight="bold" fontSize={{ base: "2rem", md: "3rem" }}>
                  94%
                </Text>
                <Text fontSize={{ base: "sm", md: "md" }}>
                  Satisfaction rate
                </Text>
              </Box>
              <Box w={{ base: 150, md: 200, lg: 250 }}>
                <Text fontWeight="bold" fontSize={{ base: "2rem", md: "3rem" }}>
                  3,500
                </Text>
                <Text fontSize={{ base: "sm", md: "md" }}>
                  Students/alumni in mentoring
                </Text>
              </Box>
            </Flex>         
          </Box>
          <Box
            w={{ base: "100%", lg: "50%", xl: "40%" }}
            minH={{ base: "auto", md: "650px" }}
          >
            <Image
              src={hero_img}
              borderRadius={"1rem"}
              objectFit={"cover"}
              objectPosition={"center"}
              alt="Success Stories"
              w={"100%"}
              height={"100%"}
            />
          </Box>
        </Flex>
      </Box>
      <Box bg={"#fff"} px={{ base: 5, md: 50 }} overflowX={"hidden"}>
        <Heading
          as={"h1"}
          fontSize={{ base: "2rem", md: "3rem" }}
          py={{ base: 2, md: 4, lg: 6 }}
          mt={10}
          textAlign={"center"}
        >
          History
        </Heading>
        <History />
      </Box>
      <Flex px={{ base: 5, md: 50 }} flexDir={{base:"column",md:'row'}}>
        <Box>
          <Heading
            as={"h1"}
            fontSize={{ base: "2rem", md: "3rem" }}
            py={{ base: 2, md: 4, lg: 6 }}
            mt={10}
          >
            Testimonials
          </Heading>
          <Text w={{ base: 350, md: 500, lg: 800 }} maxW={"400px"}>
            Discover the success stories of individuals who transformed their
            careers through Moringa School's programs.{" "}
            <Text as={"span"} display={{ base: "none", md: "inline" }}>
              From diverse backgrounds and skill sets, these alumni and alumnae
              found their paths in tech after completing rigorous training at
              Moringa.
            </Text>
          </Text>
        </Box>

        <Box mx={"auto"} mt={"40px"} w={{ base: "100%", md: "50%" }}>
          <Testimonials />
        </Box>
      </Flex>
    </Box>
  );
};

export default SuccessStories;
